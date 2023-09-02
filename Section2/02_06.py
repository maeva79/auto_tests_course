from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    input1.send_keys("Lara")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")
    input2.send_keys("Shemet")
    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")
    input3.send_keys("123@ya.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "txt.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    button = browser.find_element(By.XPATH, "//button[text()='Submit']").click()

finally:
    time.sleep(30)
    browser.quit()
