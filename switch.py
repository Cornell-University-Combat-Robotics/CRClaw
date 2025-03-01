# import RPi.GPIO as GPIO

# class Limit():

#     def __init__(self, pin):
#         GPIO.setmode(GPIO.BCM)
#         GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#         self.pin =pin

    
#     # returns true if it is pressed, false otherwise
#     def isPressed(self):
#         GPIO.input(self.pin) == GPIO.HIGH

#     def cleanup(self):
#         GPIO.cleanup()

# This Raspberry Pi code was developed by newbiely.com
# This Raspberry Pi code is made available for public use without any restriction
# For comprehensive instructions and wiring diagrams, please visit:
# https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-limit-switch


import RPi.GPIO as GPIO

class Limit():

    # SWITCH_PIN = 16
    DEBOUNCE_TIME_MS = 200  # 200 milliseconds

    def __init__(self,pin):
        self.pin = pin     # Define the GPIO pin for your button
        GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
        # Set the initial state and pull-up resistor for the button
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        # Initialize the button state and previous state
        global switch_state
        switch_state = GPIO.input(pin)
        global prev_switch_state

    # Define a function to handle button presses
    def button_callback(self):
        self.switch_state = GPIO.input(self.pin)
# Add an event listener for the button press
    def add_event(self):
        #GPIO.add_event_detect(self.pin, GPIO.BOTH, callback=self.button_callback, bouncetime=Limit.DEBOUNCE_TIME_MS)
        GPIO.add_event_detect(self.pin, GPIO.BOTH)

    def is_touched():
        # Check if the button state has changed
        if switch_state != prev_switch_state:
            if switch_state == GPIO.HIGH:
                print("The limit switch: TOUCHED -> UNTOUCHED")
            else:
                print("The limit switch: UNTOUCHED -> TOUCHED")
            
            prev_switch_state = switch_state


        if switch_state == GPIO.HIGH:
            print("The limit switch: UNTOUCHED")
        else:
            print("The limit switch: TOUCHED")

    def cleanup(self):
        GPIO.cleanup()
    
    #sardor and nick will help with this
