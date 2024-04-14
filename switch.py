import RPi.GPIO as GPIO

class Limit():

    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.pin =pin

    
    # returns true if it is pressed, false otherwise
    def isPressed(self):
        GPIO.input(self.pin) == GPIO.HIGH

    def cleanup(self):
        GPIO.cleanup()