import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, "Frames").click()
driver.find_element(By.LINK_TEXT, "iFrame").click()
driver.switch_to.frame("mce_0_ifr")

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Harshal tu chavva ahes")

driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)