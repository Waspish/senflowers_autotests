import datetime
import os.path

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, by_type, locator):
        return WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((by_type, locator)))

    def assert_word(self, element, expected_word):
        actual_word = element.text
        try:
            assert expected_word == actual_word
            print("Good value word")
        except AssertionError as error:
            self.save_screen()
            print(f"Assertion failed, expected {expected_word}, but got {actual_word}")

    def save_screen(self):
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        current_time = datetime.datetime.now().strftime('%d.%m.%Y-%H.%M.%S')
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        screens_dir = os.path.join(project_root, 'screens')
        os.makedirs(os.path.join(screens_dir, current_date), exist_ok=True)
        path = os.path.join(screens_dir, f'{current_date}', f'{current_time}.png')
        self.driver.save_screenshot(path)
        print(f"Sreenshot saved to {path}")
