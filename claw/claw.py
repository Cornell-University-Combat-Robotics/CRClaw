import RPi.GPIO as GPIO

class Claw:
    def __init__(self, motor, pin):
        self.motor = motor
        self.pin = pin

    def clamp(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def release(self):
        GPIO.output(self.pin, GPIO.LOW)
