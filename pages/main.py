from selenium.webdriver.common.by import By

from base.base import Base


class Main(Base):
    # constants
    MAIN_WORD = 'Бестселлеры'

    # locators (если 10 и больше + потом более спцифично типо LOGIN_LOCATORS...)
    LOCATORS = {
        "cart": "//a[@class='cart-link']",
        "main_word": "//p[text()='Бестселлеры']"
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # getters

    def click_cart(self):
        self.get_cart().click()
        print('Cart clicked')

    # actions

    def get_cart(self):
        return self.wait(By.XPATH, self.LOCATORS['cart'])

    def get_main_word(self):
        return self.wait(By.XPATH, self.LOCATORS['main_word'])

    # methods

    def select_product_go_cart(self):
        self.driver.get('https://sendflowers.by/')
        self.driver.maximize_window()
        self.assert_word(self.get_main_word(), self.MAIN_WORD)
        self.click_cart()
