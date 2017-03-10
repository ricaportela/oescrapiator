"""Browser."""
# coding: utf-8
from selenium import webdriver


class Browser():
    """Broser Class control open, close e navigation Firefox."""

    driver = ''

    def __init__(self, driver):
        """Constructor."""

    def access(url):
        """Navigation page."""
        print("Open webdriver")
        driver = webdriver.Firefox()
        driver.implicitly_wait(2)
        driver.get(url)
