from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
# открыть браузер
browser.get(link)

# поиск картинки, поиск значения valuex, посчитать математическую функцию от x
x_element = browser.find_element(By.ID, "treasure")
x = x_element.get_attribute("valuex")
y = calc(x)

# ввести ответ в текстовое поле
textarea = browser.find_element(By.ID, "answer").send_keys(y)

# отметить checkbox
option1 = browser.find_element(By.ID, "robotCheckbox").click()

# отметить radiobutton роботы рулят
option2 = browser.find_element(By.ID, "robotsRule").click()

# нажать Submit
button = browser.find_element(By.XPATH, "//button[text()='Submit']").click()

time.sleep(30)
browser.quit()
