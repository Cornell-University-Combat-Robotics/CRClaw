from machine import Pin

class Button:
    def __init__(self, pin_number: int):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)

    def is_pressed(self) -> bool:
        return self.pin.value() == 0