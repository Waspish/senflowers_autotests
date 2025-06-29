import allure

from pages.cart import Cart
from pages.checkout import Checkout
from pages.login import Login
from pages.main import Main
from pages.payment import Payment


@allure.description('test_buy_product')
def test_buy_product(driver):
    email = "ostapa@mailto.plus"
    password = "ostapa@mailto.plus"
    login_page = Login(driver)
    login_page.authorize(email, password)
    main_page = Main(driver)
    price, desk = main_page.select_one_product(7)
    print(price, desk)
    cart_page = Cart(driver)
    cart_page.purchase_product()
    checkout_page = Checkout(driver)
    checkout_page.purchase_product("Беларусь", "Минск")
    payment_page = Payment(driver)
    payment_page.make_payment()


@allure.description('test_buy_product_2')
def test_buy_product_2(driver):
    email = "ostapa@mailto.plus"
    password = "ostapa@mailto.plus"
    login_page = Login(driver)
    login_page.authorize(email, password)
    main_page = Main(driver)
    price, desk = main_page.select_one_product(16)
    print(price, desk)
    cart_page = Cart(driver)
    cart_page.purchase_product()
    checkout_page = Checkout(driver)
    checkout_page.purchase_product("Беларусь", "Брест")
    payment_page = Payment(driver)
    payment_page.make_payment()
