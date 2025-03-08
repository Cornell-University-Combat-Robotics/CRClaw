from time import sleep
import RPi.GPIO as GPIO # this gives us access to the pi pins

# PINs (alter to be accurate)
RELAY_IN = 20
delay = 2000

GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_IN, GPIO.OUT)

GPIO.output(RELAY_IN, GPIO.HIGH)
sleep(delay)
GPIO.output(RELAY_IN, GPIO.LOW)
sleep(delay)

GPIO.cleanup()