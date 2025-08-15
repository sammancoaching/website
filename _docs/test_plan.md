# Test Plan

## UI: Search Bar (Selenium)

Purpose: End-to-end verification that the on-site search shows results correctly.

Dependencies: Selenium (Chrome), ChromeDriver, Python requests, Ruby/Jekyll via Bundler.

Environment/Setup (from `tests/test_search_bar.py`):
- Start server: `bundle exec jekyll serve --port 4001`
- Readiness: `wait_for_server(url, max_attempts=5, base_delay=1)` with exponential backoff accepts any non-5xx status
- Browser: Headless Chrome with `webdriver.Chrome`
- Navigate to `http://localhost:4001`

Teardown:
- Quit WebDriver
- Terminate Jekyll process; on Windows also `taskkill /F /IM ruby.exe`

Test cases:

1) test_search_bar_shows_results
   - Action: Type `approval` into `#search-input` and press Enter
   - Expectation: `#search-results` becomes visible and at least one result (`li a`) contains "approval" in its title or link text
   - Notes: On failure, assertion message includes collected titles and texts for debugging

2) ignore_test_search_bar_no_results (disabled)
   - Action: Type `thisqueryshouldnotexist123` into `#search-input` and press Enter
   - Expectation: `#search-results` is not visible and its text is empty (no results)

