
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value1 = int(browser.find_element(By.ID, "num1").text)
    value2 = int(browser.find_element(By.ID, "num2").text)
    summa = str(value1 + value2)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summa)

    browser.find_element(By.CLASS_NAME, "btn-default").click()


finally:
    #успеваем скопировать код за 30 секунд
    time.sleep(30)
    #закрываем браузер после всех манипуляций
    browser.quit()
    # не забываем оставить пустую строку в конце файла