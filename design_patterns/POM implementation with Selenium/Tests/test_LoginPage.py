from Config.config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest


class TestLogin(BaseTest):
    """
    This class contains test cases for the login functionality.
    It inherits from the BaseTest class.
    """

    def test_signup_link_visible(self):
        """Test case to verify the visibility of the sign-up link on the login page."""
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exists()
        assert flag

    def test_login_page_title(self):
        """Test case to verify the title of the login page."""
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        """Test case to perform a login action."""
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
