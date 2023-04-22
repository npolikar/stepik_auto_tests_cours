# from selenium import webdriver
# import time
#
# browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robot');")
# time.sleep(5)

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

button.click()