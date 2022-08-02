from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.XPATH, "//input[@type='text']")
    for field in elements:
        field.send_keys("A")

    #browser.find_element(By.NAME, "firstname").send_keys("A")
    #browser.find_element(By.NAME, "lastname").send_keys("A")
    #browser.find_element(By.NAME, "email").send_keys("A")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
        
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
