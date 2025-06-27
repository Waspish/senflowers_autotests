from selenium.webdriver.common.by import By

from base.base import Base


class Main(Base):
    # constants
    PAGE_URL = "https://sendflowers.by/"
    MAIN_WORD = "Бестселлеры"
    FILE_NAME = "main"

    # locators
    cart = "//a[@class='cart-link']"
    main_word = "//p[text()='Бестселлеры']"

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
        self.driver.get('https://sendflowers.by/')
        self.driver.maximize_window()
        self.assert_word(self.get_main_word(), self.MAIN_WORD, self.FILE_NAME)
        self.assert_url(self.PAGE_URL, self.FILE_NAME)
        self.click_cart()
