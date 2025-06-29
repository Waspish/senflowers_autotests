import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = ChromeOptions()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get('https://sendflowers.by/')
locator = "//section[@class='product-list']/div[1]/button"

elements = driver.find_elements(By.XPATH, locator)
action = ActionChains(driver)

time.sleep(2)
action.move_to_element(elements[0]).click().perform()
time.sleep(2)
select = Select(driver.find_element(By.XPATH, "//*[@id='input-zone']"))
select.select_by_visible_text('Брест')
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='collapse-shipping']/div/div[1]/div[3]/button[1]").click()
time.sleep(2)
