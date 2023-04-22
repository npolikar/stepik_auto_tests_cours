from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))

    # button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve")))
    input = browser.find_element(By.CSS_SELECTOR, "button")
    input.click()

    number = browser.find_element(By.CSS_SELECTOR, "#input_value")
    number = number.text
    number = calc(number)


    input = browser.find_element(By.CSS_SELECTOR, ".form-control")
    input.send_keys(number)

    input = browser.find_element(By.CSS_SELECTOR, "#solve")
    input.click()

finally:
    time.sleep(10)
    browser.quit()
