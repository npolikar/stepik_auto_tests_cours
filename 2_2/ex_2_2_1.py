from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x: str):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"

    browser = webdriver.Chrome()
    browser.get(link)

    number_elem_one = browser.find_element(By.CSS_SELECTOR, ".container .nowrap:nth-child(2)")
    number1 = int(number_elem_one.text)

    number_elem_one = browser.find_element(By.CSS_SELECTOR, ".container .nowrap:nth-child(4)")
    number2 = int(number_elem_one.text)

    total = str(number1 + number2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(total)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()