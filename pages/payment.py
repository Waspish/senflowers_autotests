import allure
from selenium.webdriver.common.by import By

from base.base import Base


class Payment(Base):
    # constants
    FILE_NAME = "payment"
    SHOP_NAME = "Аромат Любви"

    # locators
    shop_name = '//span[@data-tdata="merchant.name"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # getters
    def get_shop_name(self):
        return self.wait(By.XPATH, self.shop_name)

    # actions

    # methods
    def make_payment(self):
        with allure.step('purchase_product'):
            self.assert_word(self.get_shop_name(), self.SHOP_NAME, self.FILE_NAME)
