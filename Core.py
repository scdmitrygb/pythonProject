import unittest

from selenium.webdriver.common.by import By


def by_locator(self, locator):
    if locator.startswith("/"):
        return self.browser.find_element(By.XPATH, locator)
    else:
        return self.browser.find_element(By.CSS_SELECTOR, locator)
