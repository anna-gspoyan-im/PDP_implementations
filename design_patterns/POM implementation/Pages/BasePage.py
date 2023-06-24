from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    """
    This class is the parent of all pages. It contains all the generic methods and utilities for all the pages
    """

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        """
        Perform a click action on the element located by the specified locator.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        """
        Enter the specified text into the element located by the specified locator.
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        """
        Get the text content of the element located by the specified locator.
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        """
        Check if the element located by the specified locator is visible.
        """
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        """
        Wait until the page title matches the specified title.
        """
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
