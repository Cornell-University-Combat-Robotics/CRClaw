from time import sleep
import RPi.GPIO as GPIO

pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, GPIO.HIGH)
sleep(2)

GPIO.cleanup()