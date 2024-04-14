import RPi.GPIO as GPIO

class Limit():

    def __init__(self, pin):
        self.switch_state = GPIO.input(pin)

    
    # returns true if it is pressed, false otherwise
    def isPressed(self):
        self.switch_state == GPIO.HIGH
