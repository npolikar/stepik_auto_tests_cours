from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    result = calc(input_value)

    button = browser.find_element(By.CSS_SELECTOR, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)

    browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

    # browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    radio = browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    radio.click()

    browser.find_element(By.CSS_SELECTOR, "button").click()

finally:
    time.sleep(10)
    browser.quit()
