from machine import Pin

class Sensor:
    def __init__(self, pin, sensor_type="coin"):
        self.sensor_type = sensor_type

        # try PULL_UP first (most common for break-beam sensors)
        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)

        self.last_state = self.pin.value()
        self.count = 0

    def update(self):
        current = self.pin.value()

        # Human readable status
        if current == 1:
            status = "😮 CLEAR   (beam intact)"
        else:
            status = "🫣 BLOCKED (beam broken)"

        print(f"{self.sensor_type}: {status}")

        # Detect transition (CLEAR → BLOCKED)
        if self.last_state == 1 and current == 0:
            self.count += 1
            print(f"{self.sensor_type.upper()} DETECTED! Count = {self.count}")

        self.last_state = current
        return self.count

    def reset(self):
        self.count = 0
        print(f"{self.sensor_type}: reset to 0")
