from machine import Pin

class Claw:
    def __init__(self, control_pin):
        self.control = Pin(control_pin, Pin.OUT)

    def update(self, action):
        if action == "clamp":
            self.control.value(1)
            print("Claw: clamp")
        elif action == "release":
            self.control.value(0)
            print("Claw: release")
