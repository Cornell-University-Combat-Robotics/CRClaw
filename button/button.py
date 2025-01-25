import RPi.GPIO as GPIO

class Button:
    def __init__(self, pin):
        # assign GPIO pin to self
        self.PIN = pin
    
    def is_Pressed(self):
        # poll GPIO to see if the button was pressed
        if GPIO.input(self.PIN): 
            return True 
        else: 
            return False