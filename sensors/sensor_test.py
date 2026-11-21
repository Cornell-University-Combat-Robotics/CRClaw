from sensors.sensor import Sensor
import time
from machine import Pin


sensor_pin = 2

tester = Sensor(sensor_pin, "coin")

print("Starting sensor test...")

while True:
#     pin = Pin(sensor_pin, Pin.IN, Pin.PULL_UP)
#     last_state = pin.value()
#     print(f"state: {last_state}")
    tester.update()
    time.sleep(0.01)   # fast updates = better detection
