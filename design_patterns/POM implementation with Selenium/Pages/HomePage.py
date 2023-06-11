import os

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class HomePage(BasePage):
    """
    This class represents the home page. It inherits from the BasePage class and contains specific methods for the home page.
    """
    HEADER = (By.CSS_SELECTOR, os.getenv("HEADER"))
    ACCOUNT_NAME = (By.CSS_SELECTOR, os.getenv("ACCOUNT_NAME"))
    SETTINGS_ICON = (By.ID, os.getenv("SETTINGS_ICON"))

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page_title(self, title):
        """
        Get the title of the home page.
        """
        return self.get_title(title)

    def is_settings_icon_exist(self):
        """
        Check if the settings icon is visible on the home page.
        """
        return self.is_visible(self.SETTINGS_ICON)

    def get_header_value(self):
        """
        Get the value of the header on the home page.
        """
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)

    def get_account_name_value(self):
        """
        Get the value of the account name on the home page.
        """
        if self.is_visible(self.ACCOUNT_NAME):
            return self.get_element_text(self.ACCOUNT_NAME)
