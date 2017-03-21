"""Browser."""
# coding: utf-8
from selenium import webdriver


class Browser():
    """Broser Class control open, close e navigation Firefox."""

    driver = ''

    def __init__(self, url):
        """Constructor."""
        self.url = url
        self.driver = webdriver.Firefox()

    def access(self, url):
        """Navigation page."""
        print("Open webdriver")
        try:
            self.driver.implicitly_wait(2)
            self.driver.get(url)
        except Exception as e:
            print("Connection terminated")
        else:
            print("Connection estabilished...")

        return self.driver
