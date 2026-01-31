from machine import Pin

class Joystick:
    def __init__(self, fpin, bpin, lpin, rpin):
        self.f_switch = Pin(fpin, Pin.IN, Pin.PULL_UP)
        self.b_switch = Pin(bpin, Pin.IN, Pin.PULL_UP)
        self.l_switch = Pin(lpin, Pin.IN, Pin.PULL_UP)
        self.r_switch = Pin(rpin, Pin.IN, Pin.PULL_UP)

    def update(self):
        f = self.f_switch.value() # read input from f_switch
        b = self.b_switch.value() # read input from b_switch
        l = self.l_switch.value() # read input from l_switch
        r = self.r_switch.value() # read input from b_switch
        
        print("forward: " + f)
        print("back: " + b)
        print("left: " + l)
        print("right: " + r)
        
        return [f - b, l - r]