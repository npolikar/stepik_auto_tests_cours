from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element(By.CSS_SELECTOR, "button")
    input.click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()

    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    number = number.text
    number = calc(number)

    input = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input.send_keys(number)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
