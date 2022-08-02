from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/explicit_wait2.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, "price"),'100'))

    browser.find_element(By.ID, "book").click()


    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    browser.find_element(By.ID, "solve").click()


finally:
    time.sleep(5)
    browser.quit()
