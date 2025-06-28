import allure

from pages.login import Login
from pages.main import Main


@allure.description('test_buy_product')
def test_buy_product(driver):
    email = "ostapa@mailto.plus"
    password = "ostapa@mailto.plus"
    login_page = Login(driver)
    login_page.authorize(email, password)
    main_page = Main(driver)
    main_page.select_product_go_cart()


@allure.description('test_buy_product_2')
def test_buy_product_2(driver):
    email = "ostapa@mailto.plus"
    password = "ostapa@mailto.plus"
    login_page = Login(driver)
    login_page.authorize(email, password)
    main_page = Main(driver)
    main_page.select_product_go_cart()
