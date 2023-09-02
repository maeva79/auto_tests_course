from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import pyperclip as pc

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
browser.find_element(by=By.ID, value="book").click()

x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
textarea = browser.find_element(By.ID, "answer").send_keys(y)

button = browser.find_element(By.ID, "solve").click()

pc.copy(browser.switch_to.alert.text.split(': ')[-1])
browser.quit()
