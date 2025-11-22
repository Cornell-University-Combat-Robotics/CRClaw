from machine import Pin
import utime

class Claw:
    def __init__(self, pin):
        #self.motor = motor
        self.pin = Pin(pin, Pin.OUT, Pin.PULL_DOWN)

    def clamp(self):
        self.pin.high()

    def release(self):
        self.pin.low()

if __name__ == '__main__':
    while (True):
        claw = Claw("GP26")
        claw.clamp()
        utime.sleep_ms(3000)
        claw.release()
        utime.sleep_ms(3000)