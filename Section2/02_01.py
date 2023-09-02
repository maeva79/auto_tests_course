from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
textarea = browser.find_element(By.ID, "answer").send_keys(y)

#checkbox
option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()

#radiobutton
option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()

button = browser.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(30)
browser.quit()
