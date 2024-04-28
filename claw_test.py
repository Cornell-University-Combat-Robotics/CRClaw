from time import sleep
import RPi.GPIO as GPIO

pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.output(pin, GPIO.HIGH)
sleep(.5)
GPIO.output(pin, GPIO.LOW)
