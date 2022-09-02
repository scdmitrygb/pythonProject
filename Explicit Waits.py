import math
import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Переменная на ссылку сайта
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser: WebDriver = webdriver.Chrome()

    # Говорим WebDriver ждать все элементы в течение 5 секунд
    browser.implicitly_wait(5)

    # Открываем ссылку в браузере
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    # Находим значения Х для передачи в формулу
    x = browser.find_element(By.ID, "input_value").text
    # print(x)

    # Рассчитываем формулу
    result = str(math.log(abs(12 * math.sin(int(x)))))
    print(result)

    # Находим поле для ввода значения формулы и устанавливаем значение
    browser.find_element(By.ID, "answer").send_keys(result)

    # Находим кнопку и нажимаем для отправки результата
    browser.find_element(By.ID, "solve").click()


finally:
    # Ждем 30 секунд и закрываем окно браузера
    time.sleep(30)
    browser.quit()
