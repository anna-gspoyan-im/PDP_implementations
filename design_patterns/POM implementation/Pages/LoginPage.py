from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    EMAIL = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions for Login page"""

    def get_login_page_title(self, title):
        """
        Get the title of the login page.
        """
        return self.get_title(title)

    def is_signup_link_exists(self):
        """Check if the sign up link exists on the login page."""
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        """Perform a login action on the login page."""
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)
