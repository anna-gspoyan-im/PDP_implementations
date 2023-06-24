import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class TestData:
    CHROME_EXECUTABLE_PATH = os.getenv('CHROME_EXECUTABLE_PATH')
    FIREFOX_EXECUTABLE_PATH = os.getenv('FIREFOX_EXECUTABLE_PATH')
    BASE_URL = os.getenv('BASE_URL')
    USER_NAME = os.getenv('USER_NAME')
    PASSWORD = os.getenv('PASSWORD')
    LOGIN_PAGE_TITLE = os.getenv('LOGIN_PAGE_TITLE')
    HOME_PAGE_TITLE = os.getenv('HOME_PAGE_TITLE')
    HOME_PAGE_HEADER = os.getenv('HOME_PAGE_HEADER')
    ACCOUNT_NAME = os.getenv('ACCOUNT_NAME')
