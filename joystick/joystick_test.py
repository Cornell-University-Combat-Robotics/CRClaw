from machine import Pin
from joystick import Joystick
import time

backpin = 2
leftpin = 3
frontpin = 4
rightpin = 5

tester = Joystick(frontpin, backpin, leftpin, rightpin)

while True:
    tester.update()
    time.sleep(0.2)