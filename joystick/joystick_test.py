import RPi.GPIO as GPIO

from joystick import Joystick

frontpin = 26
backpin = 16
leftpin = 5
rightpin = 6

GPIO.setmode(GPIO.BCM)

GPIO.setup(frontpin, GPIO.OUT)
GPIO.setup(backpin, GPIO.OUT)
GPIO.setup(leftpin, GPIO.OUT)
GPIO.setup(rightpin, GPIO.OUT)

tester = Joystick(self, frontpin, backpin, leftpin, rightpin)
tester.update(self)

GPIO.cleanup()