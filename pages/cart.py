import allure
from selenium.webdriver.common.by import By

from base.base import Base


class Cart(Base):
    # constants
    PAGE_URL = "https://sendflowers.by/cart"
    FILE_NAME = "cart"

    # locators
    purchase_button = '//a[text()="Оформить заказ"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # getters
    def get_purchase_button(self):
        return self.wait(By.XPATH, self.purchase_button)

    # actions
    def click_purchase_button(self):
        self.get_purchase_button().click()
        print(f'Purchase button clicked')

    # methods
    def purchase_product(self):
        with allure.step('purchase_product'):
            self.assert_url(self.PAGE_URL, self.FILE_NAME)
            self.click_purchase_button()
