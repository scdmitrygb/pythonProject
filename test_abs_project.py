import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_registration1():
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration1.html"
    browser.get(link)
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys("Ivan")
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys("Popov")
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys("popov@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!", "Удачное выполнение теста"


def test_registration2():
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys("Ivan")
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys("Popov")
    browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys("popov@mail.ru")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert welcome_text == "Congratulations! You have successfully registered!", "Ошибка"
