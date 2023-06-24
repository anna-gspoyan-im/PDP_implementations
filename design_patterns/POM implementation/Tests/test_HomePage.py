from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestHome(BaseTest):
    """
      This class contains test cases for the home page functionality.
      It inherits from the BaseTest class.
    """

    def test_home_page_title(self):
        """Test case to verify the title of the home page."""
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = home_page.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        """Test case to verify the header value on the home page."""
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = home_page.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_home_account_name(self):
        """Test case to verify the account name on the home page."""
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        account_name = home_page.get_account_name_value()
        assert account_name == TestData.ACCOUNT_NAME

    def test_settings_icon(self):
        """
        Test case to verify the presence of the settings icon on the home page.

        Steps:
        1. Log in to the application using valid credentials.
        2. Check if the settings icon is visible on the home page.
        3. Assert that the settings icon exists."""
        self.loginPage = LoginPage(self.driver)
        home_page = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert home_page.is_settings_icon_exist()
