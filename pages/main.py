import time

import allure
from selenium.webdriver.common.by import By

from base.base import Base
from utilities.logger import Logger


class Main(Base):
    # constants
    PAGE_URL = "https://sendflowers.by/my-account"
    MAIN_WORD = "Доставка цветов и подарков по Минску, Беларуси и миру!"
    FILE_NAME = "main"

    # locators
    cart = "//a[@class='cart-link']"
    main_word = "//p[text()='Доставка цветов и подарков по Минску, Беларуси и миру!']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # getters

    def get_cart(self):
        return self.wait(By.XPATH, self.cart)

    def get_main_word(self):
        return self.wait(By.XPATH, self.main_word)

    # actions

    def click_cart(self):
        self.get_cart().click()
        print('Cart clicked')

    # methods

    def select_product_go_cart(self):
        with allure.step('select_product_go_cart'):
            Logger().add_start_step('select_product_go_cart')
            # cause stale element exception
            time.sleep(0.5)
            self.assert_word(self.get_main_word(), self.MAIN_WORD, self.FILE_NAME)
            self.assert_url(self.PAGE_URL, self.FILE_NAME)
            self.click_cart()
            Logger().add_end_step(self.driver.current_url, 'select_product_go_cart')
