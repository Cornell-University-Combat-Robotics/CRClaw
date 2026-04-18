from machine import Pin
import time

button = Pin(14, Pin.IN, Pin.PULL_UP)  # change pin if needed

print("Button test started...")

while True:
    state = button.value()

    if state == 0:
        print("PRESSED")

    time.sleep(0.1)
