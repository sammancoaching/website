import time
import unittest
import subprocess
import sys
import socket
import platform
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


def wait_for_server(url, max_attempts=5, base_delay=1):
    """
    Wait for a server to be ready with exponential backoff.
    
    Args:
        url (str): The URL to check
        max_attempts (int): Maximum number of connection attempts
        base_delay (float): Initial delay between attempts in seconds
        
    Returns:
        bool: True if server is up, False otherwise
    """
    print(f"\n=== Waiting for server at {url} ===")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    for attempt in range(max_attempts):
        try:
            print(f"Attempt {attempt + 1}/{max_attempts}: Trying to connect...")
            response = requests.get(url, timeout=5)
            if response.status_code < 500:  # Accept any non-5xx status code
                print(f"SUCCESS: Server responded with status code: {response.status_code}")
                print("=== Server is up and running! ===\n")
                return True
            else:
                print(f"WARNING: Server responded with status code: {response.status_code}")
        except requests.exceptions.Timeout:
            print("INFO: Connection timed out")
        except requests.exceptions.ConnectionError as e:
            error_msg = str(e)
            if "Connection refused" in error_msg or "Failed to establish" in error_msg:
                print(f"INFO: Connection refused (server not ready yet)")
            else:
                print(f"INFO: Connection error: {error_msg[:100]}")  # Truncate long errors
        except requests.exceptions.RequestException as e:
            print(f"INFO: Request failed: {str(e)[:100]}")  # Truncate long errors
        
        if attempt < max_attempts - 1:  # Don't sleep on the last attempt
            wait_time = base_delay * (2 ** attempt)
            print(f"Waiting {wait_time} seconds before next attempt...\n")
            time.sleep(wait_time)
    
    print("\nERROR: Server failed to start after all attempts")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    return False

class TestSearchBar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Find an available port dynamically to avoid conflicts
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.listen(1)
            port = s.getsockname()[1]
        
        print(f"Starting Jekyll server on dynamically allocated port: {port}")
        cls.port = port
        cls.server_process = subprocess.Popen(
            ["bundle", "exec", "jekyll", "serve", "--port", str(port)],
            shell=platform.system() == "Windows",
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,  # Also suppress stderr to avoid conflicts
        )
        server_url = f'http://localhost:{port}'
        if not wait_for_server(server_url, max_attempts=10, base_delay=2):
            raise Exception(f"Server did not start after multiple attempts on port {port}")

        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run headless for CI
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.get(server_url)

    @classmethod
    def tearDownClass(cls):
        print(f"\nCleaning up: Stopping Jekyll server on port {cls.port}")
        cls.driver.quit()
        
        # Terminate the server process gracefully first
        cls.server_process.terminate()
        try:
            cls.server_process.wait(timeout=5)
            print("Jekyll server terminated gracefully")
        except subprocess.TimeoutExpired:
            print("Jekyll server did not terminate gracefully, forcing kill")
            cls.server_process.kill()
            cls.server_process.wait(timeout=5)
        
        # On Windows, ensure all Ruby processes are killed to avoid port conflicts
        if sys.platform.startswith('win'):
            print("Cleaning up any remaining Ruby processes on Windows")
            subprocess.call("taskkill.exe /F /im ruby.exe", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Give a small delay to ensure port is released
        time.sleep(1)
        print("Cleanup completed")

    def test_search_bar_shows_results(self):
        driver = self.driver
        search_input = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, 'search-input'))
        )
        search_input.clear()
        search_input.send_keys('approval')
        search_input.send_keys(Keys.RETURN)

        # Assert that at least one result contains 'approval' in the title or text
        found = False
        # Wait for search results to be visible
        results = WebDriverWait(driver, 100).until(
            expected_conditions.visibility_of_element_located((By.ID, 'search-results'))
        )
        all_results = results.find_elements(By.TAG_NAME, 'li')
        all_titles = []
        all_texts = []
        for li in all_results:
            link = li.find_element(By.TAG_NAME, 'a')
            all_titles.append(link.get_attribute('title'))
            all_texts.append(link.text)
            if 'approval' in link.get_attribute('title').lower() or 'approval' in link.text.lower():
               found = True
               break
        self.assertTrue(found, f"No search result contains 'approval' in the title or text. {all_titles=} {all_texts=}")


    def ignore_test_search_bar_no_results(self):
        driver = self.driver
        search_input = WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, 'search-input'))
        )
        search_input.clear()
        search_input.send_keys('thisqueryshouldnotexist123')
        search_input.send_keys(Keys.RETURN)
        # Expectation: results container is NOT visible and its text is empty
        # Wait until the results container is invisible or not present
        WebDriverWait(driver, 10).until(
            expected_conditions.invisibility_of_element_located((By.ID, 'search-results'))
        )
        # Verify: not visible AND empty text. If element is absent, treat as not visible with empty text
        try:
            results = driver.find_element(By.ID, 'search-results')
            self.assertFalse(results.is_displayed(), "Expected #search-results to be not visible")
            self.assertEqual('', results.text)
        except NoSuchElementException:
            # Not present implies not visible, and we consider text to be empty
            pass

if __name__ == '__main__':
    unittest.main()
