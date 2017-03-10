"""Main Module."""
from app.browser import Browser
from app.displayonoff import DisplayOnOff

BASE_URL = "https://www.revistanatura.com.br/html/widget"


if __name__ == "__main__":
    # import pdb; pdb.set_trace()
    print("Executing script...")

    DisplayOnOff.open_virtual_display
    Browser.access(BASE_URL)
    # try:

    # except Exception as e:
    #    print("ferrou")
    # else:
    #     print("ok abriu...")

    DisplayOnOff.stop_virtual_display()
