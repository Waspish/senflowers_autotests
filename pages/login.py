from selenium.webdriver.common.by import By

from base.base import Base


class Login(Base):
    # constants
    PAGE_URL = "https://sendflowers.by/login"
    AUTHORIZATION_WORD = "Авторизация"
    FILE_NAME = "login"

    # locators

    authorization_word = "//h2[text()='Авторизация']"
    email_input = "input-email"
    password_input = "input-password"
    login_button = "//button[text() = 'Войти']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # getters

    def get_authorization_word(self):
        return self.wait(By.XPATH, self.authorization_word)

    def get_email_input(self):
        return self.wait(By.ID, self.email_input)

    def get_password_input(self):
        return self.wait(By.ID, self.password_input)

    def get_login_button(self):
        return self.wait(By.XPATH, self.login_button)

    # actions

    def fill_email_input(self, email_text):
        self.get_email_input().send_keys(email_text)
        print("Email filled")

    def fill_password_input(self, password_text):
        self.get_password_input().send_keys(password_text)
        print("Password filled")

    def click_login_button(self):
        self.get_login_button().click()
        print("Login button clicked")

    # methods

    def authorize(self, email_text, password_text):
        self.driver.get(self.LOGIN_PAGE)
        self.driver.maximize_window()
        self.assert_word(self.get_authorization_word(), self.AUTHORIZATION_WORD, self.FILE_NAME)
        self.assert_url(self.PAGE_URL, self.FILE_NAME)
        self.fill_email_input(email_text)
        self.fill_password_input(password_text)
        self.click_login_button()
