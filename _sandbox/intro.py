"""
Selenium with Python
https://selenium-python.readthedocs.io/
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.python.org")
driver.close()
