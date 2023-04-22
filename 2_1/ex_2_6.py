from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"

    browser = webdriver.Chrome()
    browser.get(link)

    number_elem = browser.find_element(By.CSS_SELECTOR, "#treasure")
    number = number_elem.get_attribute("valuex")
    print(number)

    number = calc(number)
    # text input
    input = browser.find_element(By.CSS_SELECTOR, ".form-group [type='text']")
    input.send_keys(number)

    checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()