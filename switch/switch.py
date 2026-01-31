from machine import Pin

class Limit():
    def __init__(self, pin_number: int):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)

    def is_touched(self):
        switch_state = self.pin.value()
        return switch_state == 1