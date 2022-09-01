
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os
from selenium.webdriver.support.select import Select
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.TAG_NAME, "button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element(By.ID, "input_value").text
    print(x)
    result = str(math.log(abs(12 * math.sin(int(x)))))
    print(result)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    #успеваем скопировать код за 30 секунд
    time.sleep(30)
    #закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла