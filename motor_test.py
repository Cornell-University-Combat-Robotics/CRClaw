from time import sleep
import RPi.GPIO as GPIO # this gives us access to the pi pins

# PINs (alter to be accurate)
DIR = 20 # direction GPIO pin
STEP = 21 # step GPIO pin


CW = 1 # clockwise
CCW = 0 # counterclockwise