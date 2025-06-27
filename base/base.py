import datetime
import os.path

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # constants
    LOGIN_PAGE = 'https://sendflowers.by/login'

    def __init__(self, driver):
        self.driver = driver

    def wait(self, by_type, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((by_type, locator)))

    def assert_word(self, element, expected_word, folder_name):
        actual_word = element.text
        try:
            assert expected_word == actual_word
            print("Good value word")
        except AssertionError as error:
            self.save_screen(folder_name)
            print(f"Assertion failed, expected WORD is {expected_word}, but got {actual_word}")

    def assert_url(self, expected_url, folder_name):
        actual_url = self.driver.current_url
        try:
            assert expected_url == actual_url
            print("Good value URL")
        except AssertionError as error:
            self.save_screen(folder_name)
            print(f"Assertion failed, expected URL is {expected_url}, but got {actual_url}")

    def save_screen(self, folder_name):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        current_time = datetime.datetime.now().strftime('%d.%m.%Y-%H.%M.%S')
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        screens_dir = os.path.join(project_root, 'screens')
        date_dir = os.path.join(screens_dir, folder_name, current_date)
        os.makedirs(date_dir, exist_ok=True)
        path = os.path.join(date_dir, f'{current_time}.png')
        self.driver.save_screenshot(path)
        print(f"Sreenshot saved to {path}")
