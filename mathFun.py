import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v101 import browser

x = browser.find_element(By.ID, "input_value").text
result = str(math.log(abs(12 * math.sin(int(x)))))
