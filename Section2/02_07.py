from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pyperclip as pc

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
time.sleep(5)

try:
    button = browser.find_element(By.XPATH, "/html/body/form/div/div/button")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.XPATH, "//*[@id='input_value']")
    x = x_element.text
    answer = calc(x)
    textarea = browser.find_element(By.ID, "answer").send_keys(answer)

    submit2 = browser.find_element(By.XPATH, "/html/body/form/div/div/button").click()

    pc.copy(browser.switch_to.alert.text.split(': ')[-1])

finally:
    time.sleep(3)
    browser.quit()
