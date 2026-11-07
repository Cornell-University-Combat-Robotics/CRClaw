import rp2
from machine import Pin
import utime

step = Pin(17, Pin.OUT, value=0)
direction = Pin(16, Pin.OUT, value=0)
logic_power = Pin(12, Pin.OUT)
logic_power.value(1)
print("Made it here")
# To control speed just modify the amount/value of nop[dely amount 0-31].
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def move():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    wrap()

"""Instantiate a state machine with the move
program, at 100000Hz, with set base to step pin."""
motor = rp2.StateMachine(0, move, freq=100000, set_base=step)

try:
    direction.value(0)
    motor.active(1)
    print ("original start")
    while True:
        utime.sleep(5)      # keeps the script alive; Ctrl+C / Stop lands here
        print("motor cc silly")
        direction.value(1)
        utime.sleep(5)
        print("motor died") # when the code if off, there is holding current 
        motor.active(0)
        utime.sleep(5)
        print("motor alive")
        print("motor cw silly")
        direction.value(0)
        motor.active(1)
        
except KeyboardInterrupt:
    pass
finally:
    motor.active(0)          # stop the PIO state machine
    motor.exec("set(pins, 0)")  # force STEP low
    direction.value(0)       # force DIR low
    print("Motor stopped")
