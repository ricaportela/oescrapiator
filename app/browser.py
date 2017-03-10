"""Browser."""
# coding: utf-8
from selenium import webdriver


class Browser():
    """Broser Class control open, close e navigation Firefox."""

    driver = ''

    def __init__(self, driver):
        """Constructor."""
        self.driver = driver

    def access(url):
        """Navigation page."""
        print("Open webdriver")
        try:
            driver = webdriver.Firefox()
            driver.implicitly_wait(2)
            driver.get(url)
        except Exception as e:
            print("Connection terminated")
        else:
            print("Connection estabilished...")

        return driver
