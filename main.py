
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    value = browser.find_element(By.XPATH, "//*[@id='input_value']")
    value_text = value.text
    print(value_text)
    matFun = math.log(abs(12*math.sin(int(value_text))))

    browser.find_element(By.ID, "answer").send_keys(matFun)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.XPATH, "/html/body/div/form/button").click()


finally:
    #успеваем скопировать код за 30 секунд
    time.sleep(30)
    #закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла