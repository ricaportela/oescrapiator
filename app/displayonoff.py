"""Set display on/off."""
from pyvirtualdisplay import Display


class DisplayOnOff():
    """Display on/off Browser."""

    display = ''

    def __init__(self, display):
        """Contructor."""
        self.display = display

    def open_virtual_display():
        """Turn of browser display."""
        display = Display(visible=0, size=(100, 100))
        display.start()

    def stop_virtual_display():
        """Set display normal."""
        display.stop()
