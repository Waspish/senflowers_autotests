from pages.login import Login
from pages.main import Main


def test_select_product(driver):
    main_page = Main(driver)
    main_page.select_product_go_cart()
    driver.quit()


def test_authorize(driver):
    email = "ostapa@mailto.plus"
    password = "ostapa@mailto.plus"
    login_page = Login(driver)
    login_page.authorize(email, password)
    driver.quit()
