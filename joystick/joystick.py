import RPi.GPIO as GPIO

class Joystick:
    def __init__(self, fpin, bpin, lpin, rpin):
        self.f_switch = fpin
        self.b_switch = bpin
        self.l_switch = lpin
        self.r_switch = rpin

        # Set up GPIO pins as input
        GPIO.setmode(GPIO.BCM)  # or GPIO.BOARD if you're using board numbering
        GPIO.setup(self.f_switch, GPIO.IN)
        GPIO.setup(self.b_switch, GPIO.IN)
        GPIO.setup(self.l_switch, GPIO.IN)
        GPIO.setup(self.r_switch, GPIO.IN)

    def update(self):
        # Read input from the switches
        f = GPIO.input(self.f_switch) # read input from f_switch
        b = GPIO.input(self.b_switch)# read input from b_switch
        l = GPIO.input(self.l_switch) # read input from l_switch
        r = GPIO.input(self.r_switch) # read input from r_switch
        
        print("forward: " + f)
        print("back: " + b)
        print("left: " + l)
        print("right: " + r)
        
        return [f - b, l - r]