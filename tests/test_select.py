from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.main import Main

options = ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--guest')


def test_select_product():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    main_page = Main(driver)
    main_page.select_product_go_cart()
    driver.quit()


def test_select_product_2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    main_page = Main(driver)
    main_page.select_product_go_cart()
    driver.quit()
