import pytest
from selenium import webdriver

from Config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    """
    This fixture provides a WebDriver instance for test classes, allowing tests to be run with different browser options.
    The fixture parameter determines the browser to use: "chrome" or "firefox".
    """
    if request.param == "chrome":
        web_driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(TestData.FIREFOX_EXECUTABLE_PATH)
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
