import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)
driver.find_element(By.ID, "openwindow").click()

windows = driver.window_handles
driver.switch_to.window(windows[1])
#we are in child window now
print(driver.find_element(By.CLASS_NAME,"cont").text\n)

driver.switch_to.window(windows[0])
#we are in parent window now
print(driver.find_element(By.ID,"openwindow").text)
