import time
import unittest
import subprocess
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestSearchBar(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the server using subprocess
        if sys.platform.startswith('win'):
            # On Windows, use the .cmd script
            cls.server_process = subprocess.Popen(['cmd', '/c', 'build_and_run.cmd'])
        else:
            cls.server_process = subprocess.Popen(['./build_and_run'])
        time.sleep(20)  # Give the server time to start

        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run headless for CI
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=chrome_options)
        # Adjust this URL as needed for your local dev server
        cls.driver.get('http://localhost:4000/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # Terminate the server process
        cls.server_process.terminate()
        try:
            cls.server_process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            cls.server_process.kill()

    def test_search_bar_shows_results(self):
        driver = self.driver
        search_input = driver.find_element(By.ID, 'search-input')
        search_input.clear()
        search_input.send_keys('approval')
        search_input.send_keys(Keys.RETURN)
        time.sleep(1)  # Wait for search results to load
        results = driver.find_element(By.ID, 'search-results')
        # Assert that at least one result contains 'approval' in the title or text
        found = False
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

    def test_search_bar_no_results(self):
        driver = self.driver
        search_input = driver.find_element(By.ID, 'search-input')
        search_input.clear()
        search_input.send_keys('thisqueryshouldnotexist123')
        search_input.send_keys(Keys.RETURN)
        time.sleep(1)
        results = driver.find_element(By.ID, 'search-results')
        self.assertEqual('', results.text)

if __name__ == '__main__':
    unittest.main()
