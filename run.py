"""Main Module."""
from app.browser import Browser
from app.scrapent import Scrapernt
from app.displayonoff import DisplayOnOff

BASE_URL = "https://www.revistanatura.com.br/html/widget"


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    print("Executing script...")
    try:
        DisplayOnOff.open_virtual_display
    except Exception as e:
        print("Display problem")
    else:
        print("Display off")

    Browser.access(BASE_URL)
    Scrapernt.consultants_list(Browser.driver)
    DisplayOnOff.stop_virtual_display()
