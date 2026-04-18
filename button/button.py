from machine import Pin
import time

class Button:
    def __init__(self, pin_number: int, name="button", debounce_ms=50):
        self.pin = Pin(pin_number, Pin.IN, Pin.PULL_UP)
        self.name = name

        self.last_state = self.pin.value()
        self.count = 0

        self.debounce_ms = debounce_ms
        self.last_time = time.ticks_ms()

    def update(self):
        current = self.pin.value()
        now = time.ticks_ms()

        pressed_event = False

        # Detect press (RELEASED → PRESSED)
        if (
            self.last_state == 1 and current == 0 and
            time.ticks_diff(now, self.last_time) > self.debounce_ms
        ):
            self.count += 1
            self.last_time = now
            pressed_event = True

        self.last_state = current
        return pressed_event

    def is_pressed(self) -> bool:
        return self.pin.value() == 0

    def reset(self):
        self.count = 0
        print(f"{self.name}: reset to 0")
