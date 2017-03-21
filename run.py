"""Main module."""
from app.scrapent2 import Browse_Webdriver

# uso para testar localmente - URL = "file:///home/ricpds/my_projects/crawler-fb/html/index.html"
URL = "https://www.revistanatura.com.br/html/widget"


if __name__ == "__main__":
    drv1 = Browse_Webdriver.open_browser_webdriver()
    Browse_Webdriver.open_link(drv1, URL)
    drv1.implicitly_wait(3)
    drv1.quit()
