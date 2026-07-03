To build and serve the site locally (http://localhost:4000), run:

    ./build_and_run

When changing styling and other small changes within a page there is no need to run the tests, the user will test the changes interactively.

When adding or removing pages, changing javascript or other larger changes, build and run the tests: 

    ./build_and_test

The search bar tests need a Chrome/Chromium browser. In environments without a standard Chrome install, set CHROME_BIN to the browser binary (e.g. CHROME_BIN=/opt/pw-browsers/chromium in Claude Code remote containers). If an incompatible chromedriver is on PATH, remove its directory from PATH so Selenium can download a matching driver.
