from sensor import Sensor
import time

sensor_pin = 11

tester = Sensor(sensor_pin, "coin")

print("Starting sensor test...")

while True:
    tester.update()
    time.sleep(0.1)   # fast updates = better detection
