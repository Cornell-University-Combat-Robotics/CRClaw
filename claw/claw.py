from machine import Pin

class Claw:
    def __init__(self, motor, pin):
        self.motor = Pin(motor, mode=Pin.OUT)
        self.pin = Pin(pin, mode=Pin.OUT)

    def clamp(self):
        self.pin.value(1)

    def release(self):
        self.pin.value(0)