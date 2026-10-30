from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


def test_search_bar_shows_results(selenium_driver):
    driver = selenium_driver
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
    assert found, f"No search result contains 'approval' in the title or text. {all_titles=} {all_texts=}"


def test_search_bar_no_results(selenium_driver):
    driver = selenium_driver
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
        assert not results.is_displayed(), "Expected #search-results to be not visible"
        assert results.text == ''
    except NoSuchElementException:
        # Not present implies not visible, and we consider text to be empty
        pass
