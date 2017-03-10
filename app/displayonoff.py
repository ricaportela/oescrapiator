"""Set display on/off."""
from pyvirtualdisplay import Display


class DisplayOnOff():
    """Display on/off Browser."""

    def __init__(self, display):
        """Contructor."""
        self.display = display

    def open_virtual_display():
        """Turn of browser display."""
        self.display = Display(visible=1, size=(100, 100))
        self.display.start()

    def stop_virtual_display():
        """Set display normal."""
        self.display.stop()
