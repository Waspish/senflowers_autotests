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
    price, desk = main_page.select_one_product('Брест', 7)
    print(price, desk)


@allure.description('test_buy_product_2')
def test_buy_product_2(driver):
    email = "ostapa@mailto.plus"
    password = "ostapa@mailto.plus"
    login_page = Login(driver)
    login_page.authorize(email, password)
    main_page = Main(driver)
    price, desk = main_page.select_one_product('Минск', 16)
    print(price, desk)
