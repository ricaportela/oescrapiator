from pyvirtualdisplay import Display


class DisplayOnOff():

    def open_virtual_display():
        """Turn of browser display """
        display = Display(visible=0, size=(100, 100))
        display.start()

    def stop_virtual_display():
        display.stop()
