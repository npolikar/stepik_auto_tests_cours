from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    number_elem = browser.find_element(By.CSS_SELECTOR, ".form-group .nowrap:nth-child(2)")
    number = number_elem.text

    number = calc(number)
    input = browser.find_element(By.CSS_SELECTOR, ".form-group .form-control")
    input.send_keys(number)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()