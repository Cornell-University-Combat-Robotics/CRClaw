import RPi.GPIO as GPIO

class Motor:
    def __init__(self, dir_pin, step_pin):
        self.dir_pin = dir_pin
        self.step_pin = step_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)  # set initial direction? when/why?

    def move(self, power, direction):
        if power == 1:
            GPIO.output(self.step_pin, GPIO.HIGH)
            GPIO.output(self.dir_pin,direction)
        else:
            GPIO.output(self.step_pin, GPIO.LOW)
