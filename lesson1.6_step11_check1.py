from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#from webdriver_manager.chrome import ChromeDriverManager

link = "http://suninjuly.github.io/registration2.html "
driver = webdriver.Chrome()
try:
    driver.get(link)
    # Ваш код, который заполняет обязательные поля
    placeholders = ["Input your first name","Input your last name","Input your email"]
    for i in placeholders:
        driver.find_element(By.CSS_SELECTOR,f"[placeholder='{i}']").send_keys('i')





    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text





finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)

    # закрываем браузер после всех манипуляций
    driver.quit()