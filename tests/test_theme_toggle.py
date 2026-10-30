# Checks the light/dark switch in the header: clicking it changes the theme,
# and the choice carries over to the next page.
from selenium.webdriver.common.by import By


def page_theme(driver):
    return driver.execute_script("return getComputedStyle(document.documentElement).colorScheme")


def test_theme_toggle_switches_theme_and_remembers_it(selenium_driver):
    driver = selenium_driver
    driver.get(driver.server_url + '/')
    driver.execute_script("localStorage.removeItem('theme')")
    driver.get(driver.server_url + '/')
    assert page_theme(driver) == 'light'

    toggle = driver.find_element(By.CSS_SELECTOR, '.theme-toggle')
    toggle.click()
    assert page_theme(driver) == 'dark'
    assert toggle.get_attribute('aria-pressed') == 'true'

    driver.get(driver.server_url + '/society/')
    assert page_theme(driver) == 'dark'
    toggle = driver.find_element(By.CSS_SELECTOR, '.theme-toggle')
    assert toggle.get_attribute('aria-pressed') == 'true'

    toggle.click()
    assert page_theme(driver) == 'light'
    driver.get(driver.server_url + '/')
    assert page_theme(driver) == 'light'
    driver.execute_script("localStorage.removeItem('theme')")
