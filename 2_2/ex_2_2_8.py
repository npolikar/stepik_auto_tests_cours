import os
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


curr_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(curr_dir, 'file.txt')

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    fn = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    fn.send_keys("name")
    fn = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    fn.send_keys("surname")
    fn = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    fn.send_keys("email")

    file = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    file.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()
