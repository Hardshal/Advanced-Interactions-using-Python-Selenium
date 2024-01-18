from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get_screenshot_as_png()
driver.get_screenshot_as_file("shot.png")