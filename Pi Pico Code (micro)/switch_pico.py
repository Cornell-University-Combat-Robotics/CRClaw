from machine import Pin
import time

class Limit:
    DEBOUNCE_TIME_MS = 100  # 100 milliseconds, how fast the button registers it 

    def __init__(self, pin_num):
        # Initialize the pin as input with pull-up resistor
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
        # Store switch state
        self.switch_state = self.pin.value()
        self.prev_switch_state = self.switch_state
        self.last_debounce_time = 0

    def button_callback(self):
        # No direct equivalent of event detection callback in standard MicroPython,
        # you usually poll in a loop or use IRQ, but IRQ needs careful debouncing.
        # This function can be called from an IRQ or polling loop.
        self.switch_state = self.pin.value()

    def is_touched(self):
        current_time = time.ticks_ms()
        reading = self.pin.value()

        # Basic debounce check
        if reading != self.prev_switch_state:
            self.last_debounce_time = current_time

        if (time.ticks_diff(current_time, self.last_debounce_time) > self.DEBOUNCE_TIME_MS):
            if reading != self.switch_state:
                self.switch_state = reading
                if self.switch_state == 1: # printing transition 
                    print("The limit switch: TOUCHED -> UNTOUCHED")
                else:
                    print("The limit switch: UNTOUCHED -> TOUCHED")

        self.prev_switch_state = reading

    #printing the current state 
        # if self.switch_state == 1:
        #     print("The limit switch: UNTOUCHED")
        # else:
        #     print("The limit switch: TOUCHED")

    def cleanup(self):
        # On Pico, you generally don't need cleanup like on Raspberry Pi 4 GPIO
        pass

switch = Limit(9) # GPIO number 
try:
    while True:
        switch.is_touched()
        # time.sleep(0.1)

except KeyboardInterrupt:
    switch.cleanup()
    print("program stopped")
    # break