import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()
options.add_argument('--incognito')
options.add_argument('--guest')


@pytest.fixture
def driver():
    yield webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
