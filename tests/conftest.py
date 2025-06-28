import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--guest')
options.add_argument('--headless')


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
