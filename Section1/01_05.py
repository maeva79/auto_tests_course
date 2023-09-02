from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Lara")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Shemet")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("RnD")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "body > div > form > button")
    button.click()

finally:
    time.sleep(90)
    browser.quit()