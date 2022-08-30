"""

作者：梁明 
创建：2022/8/30 12:29
更新：2022/8/30 12:29
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "http://123.56.65.248:8080/index"
browser = webdriver.Chrome()
browser.get(url=url)

time.sleep(3)

browser.find_element(By.ID, "pwd_login").click()
browser.find_element(By.ID, "phone").send_keys("15989222305")
browser.find_element(By.ID, "pwd").send_keys("123456")
browser.find_element(By.ID, "pwd_login_btn").click()

time.sleep(2)


browser.quit()