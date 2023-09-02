from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
textarea = browser.find_element(By.ID, "answer").send_keys(y)

option1 = browser.find_element(By.ID, "robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()

option2 = browser.find_element(By.ID, "robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
option2.click()

button = browser.find_element(By.XPATH, "//button[text()='Submit']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(30)
browser.quit()
