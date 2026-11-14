import rp2
from machine import Pin

class Motor:
    def __init__(self, dir_pin, step_pin):
        self.dir = Pin(dir_pin, Pin.OUT)
        self.step = Pin(step_pin, Pin.OUT)
        
        """Instantiate a state machine with the move
        program, at 100000Hz, with set base to step pin."""
        motor = rp2.StateMachine(0, Motor.spin, freq=100000, set_base=self.step)


    # To control speed just modify the amount/value of nop[dely amount 0-31].
    @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
    def spin():
        wrap_target()
        set(pins, 1)   [31]
        nop()          [31]
        nop()          [31]
        set(pins, 0)   [31]
        nop()          [31]
        nop()          [31]
        wrap()

    def move(self, direction):
        ''' make the motors move. Direction can be 0 or 1'''
        self.dir.value(direction)
        self.motor.active(1)

    def stop(self):
        ''' stop motor '''
        self.motor.active(0) 
