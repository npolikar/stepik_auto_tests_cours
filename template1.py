from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    number = number.text
    number = calc(number)


    input = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input.send_keys(number)

    # button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
    # input = browser.find_element(By.CSS_SELECTOR, "button")
    # input.click()

finally:
    time.sleep(10)
    browser.quit()
