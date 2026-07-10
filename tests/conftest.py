import os

import pytest
from approvaltests import set_default_reporter
from approvaltests.reporters import PythonNativeReporter


@pytest.fixture(scope="session", autouse=True)
def configure_approvaltests_reporter():
    # Agents and CI can't use a GUI diff tool; humans running locally still get one.
    if os.environ.get("CLAUDECODE") or os.environ.get("CI"):
        set_default_reporter(PythonNativeReporter())
