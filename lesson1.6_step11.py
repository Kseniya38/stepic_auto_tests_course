from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

try: 
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link2)

    # Ваш код, который заполняет обязательные поля

    # Вариант, где ошибка обработана
    #elements = browser.find_elements(By.XPATH, "//input[@required]")
    #for element in elements:
    #    element.send_keys("A")
    #if len(elements) < 3:
    #    sys.exit("error")

    # Вариант, где ошибка не обработана
    input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block .first")
    input1.send_keys("A")
    input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block .second")
    input2.send_keys("A")
    input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block .third")
    input3.send_keys("A")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
