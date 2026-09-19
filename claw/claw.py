from machine import Pin

class Claw:
    def __init__(self, motor_pin, control_pin):
        self.control = Pin(control_pin, Pin.OUT)
        # TODO: initialize the motor
    
    def clamp(self):
        self.control.value(1)

    def release(self):
        self.control.value(0)
    
    def go_down(self):
        pass # TODO: make the claw go down
    
    def go_up(self):
        pass # TODO: make the claw go up