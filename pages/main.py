import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
    product = "//section[@class='product-list']/div"
    product_button = "/button"
    product_price = "//span[@data-price-type='new']"
    product_desc = "//span[@class]"

    city_dropdown_id = "input-zone"
    logo_id = "logo"
    approve_button = "//button[text()='Подтвердить']"

    def __init__(self, driver):
        super().__init__(driver)
        self.ACTION = ActionChains(driver)
        self.driver = driver

    # getters
    def get_product_desc(self):
        return self.wait(By.XPATH, self.product + self.product_desc)

    def get_product_price(self):
        return self.wait(By.XPATH, self.product + self.product_price)

    def get_approve_button(self):
        return self.wait(By.XPATH, self.approve_button)

    def get_logo(self):
        return self.wait(By.ID, self.logo_id)

    def get_city_dropdown(self):
        return Select(self.wait(By.ID, self.city_dropdown_id))

    def get_product(self):
        return self.wait(By.XPATH, self.product + self.product_button)

    def get_cart(self):
        return self.wait(By.XPATH, self.cart)

    def get_main_word(self):
        return self.wait(By.XPATH, self.main_word)

    # actions
    def click_approve_button(self):
        self.get_approve_button().click()
        print(f'Approve button clicked')

    def click_logo(self):
        self.get_logo().click()
        print(f'Logo clicked')

    def select_city_dropdown(self, city_name):
        select = self.get_city_dropdown()
        select.select_by_visible_text(city_name)
        print(f'City {city_name} selected from dropdown')

    def click_product(self):
        self.ACTION.move_to_element(self.get_product()).click().perform()
        print('Product clicked')

    def click_cart(self):
        self.get_cart().click()
        print('Cart clicked')

    # methods

    def select_one_product(self, city_name, product_number):
        with allure.step('select_one_product'):
            Logger().add_start_step('select_product_go_cart')

            # cause stale element exception
            time.sleep(0.5)

            self.assert_word(self.get_main_word(), self.MAIN_WORD, self.FILE_NAME)
            self.assert_url(self.PAGE_URL, self.FILE_NAME)

            self.click_logo()
            self.product += f'[{product_number}]'
            self.click_product()
            self.select_city_dropdown(city_name)
            self.click_approve_button()

            Logger().add_end_step(self.driver.current_url, 'select_product_go_cart')

            return self.get_product_price().text, self.get_product_desc().text
