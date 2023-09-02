from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

a_element = browser.find_element(By.ID, "num1")
b_element = browser.find_element(By.ID, "num2")
a = a_element.text
b = a_element.text
x = (int(a)+int(b))

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(x))

button = browser.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(30)
browser.quit()
