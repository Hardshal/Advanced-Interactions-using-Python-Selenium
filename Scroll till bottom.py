from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
