"""Set display on/off."""
from pyvirtualdisplay import Display


class DisplayOnOff():
    """Display on/off Browser."""

    def __init__(self, display):
        """Contructor."""
        pass

    def open_virtual_display(self):
        """Turn of browser display."""
        display = Display(visible=0, size=(100, 100))
        display.start()

    def stop_virtual_display():
        """Set display normal."""
        display.stop()
