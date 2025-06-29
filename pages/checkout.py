import time

import allure
from faker import Faker
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base import Base


class Checkout(Base):
    # constants
    PAGE_URL = "https://sendflowers.by/checkout"
    FILE_NAME = "checkout"

    # locators
    full_name_id = "shipping_address_firstname"
    receiver_phone_id = "shipping_address_field21"
    delivery_address_id = "shipping_address_address_1"
    country_dropdown_id = "shipping_address_country_id"
    city_dropdown_id = "shipping_address_zone_id"
    message_id = "comment"
    additional_info_id = "customer_field26"
    your_full_name_id = "customer_field31"
    your_country_id = "customer_field27"
    your_phone_id = "customer_telephone"
    be_paid_radio = "//input[@id='begateway']"
    checkout_button = "simplecheckout_button_confirm"

    def __init__(self, driver):
        super().__init__(driver)
        self.faker = Faker('ru_RU')
        self.driver = driver
        self.ACTION = ActionChains(driver)

    # getters
    def get_full_name(self):
        return self.wait(By.ID, self.full_name_id)

    def get_receiver_phone(self):
        return self.wait(By.ID, self.receiver_phone_id)

    def get_delivery_address(self):
        return self.wait(By.ID, self.delivery_address_id)

    def get_country_dropdown(self):
        return Select(self.wait(By.ID, self.country_dropdown_id))

    def get_city_dropdown(self):
        return Select(self.wait(By.ID, self.city_dropdown_id))

    def get_message(self):
        return self.wait(By.ID, self.message_id)

    def get_additional_info(self):
        return self.wait(By.ID, self.additional_info_id)

    def get_your_full_name(self):
        return self.wait(By.ID, self.your_full_name_id)

    def get_your_country(self):
        return self.wait(By.ID, self.your_country_id)

    def get_your_phone(self):
        return self.wait(By.ID, self.your_phone_id)

    def get_be_paid_radio(self):
        return self.wait(By.XPATH, self.be_paid_radio)

    def get_checkout_button(self):
        return self.wait(By.ID, self.checkout_button)

    # actions
    def fill_full_name(self):
        self.get_full_name().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE + self.faker.name())

        print(f'Full name filled')

    def fill_receiver_phone(self):
        self.get_receiver_phone().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
        self.get_receiver_phone().send_keys(self.faker.phone_number())
        print(f'Reciever phone filled')

    def fill_delivery_address(self):
        self.get_delivery_address().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE + self.faker.address())
        print(f'Delivery address filled')

    def select_country_dropdown(self, country_name):
        self.get_country_dropdown().select_by_visible_text(country_name)
        print(f'Country selected')

    def select_city_dropdown(self, city_name):
        self.get_city_dropdown().select_by_visible_text(city_name)
        print(f'City selected')

    def fill_message(self):
        self.get_message().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE + self.faker.text())
        print(f'Message filled')

    def fill_additional_info(self):
        self.get_additional_info().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE + self.faker.text())
        print(f'Additional info filled')

    def fill_your_full_name(self):
        self.get_your_full_name().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE + self.faker.name())
        print(f'Full name filled')

    def fill_your_country(self):
        self.get_your_country().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE + self.faker.country())
        print(f'Country filled')

    def fill_your_phone(self):
        self.get_your_phone().send_keys(Keys.CONTROL + 'a' + Keys.BACKSPACE)
        self.get_your_phone().send_keys(self.faker.phone_number())
        print(f'Full name filled')

    def select_be_paid_radio(self):
        self.get_be_paid_radio().click()
        print(f'Be paid radio selected')

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print(f'Checkout button clicked')

    # methods
    def purchase_product(self, country_name, city_name):
        with allure.step('purchase_product'):
            self.assert_url(self.PAGE_URL, self.FILE_NAME)
            self.fill_full_name()
            self.fill_receiver_phone()
            self.fill_delivery_address()
            self.select_country_dropdown(country_name)
            self.select_city_dropdown(city_name)
            self.fill_message()
            self.fill_additional_info()
            self.driver.execute_script("window.scrollTo(0,1000)")
            time.sleep(1)
            self.fill_your_full_name()
            self.fill_your_country()
            self.fill_your_phone()
            self.click_checkout_button()
