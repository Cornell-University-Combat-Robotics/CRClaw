import rp2
from machine import Pin, ADC
import utime
import time

step = Pin(17)
direction = Pin(16, Pin.OUT)
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
motor = rp2.StateMachine(0, move, freq=16000, set_base=step)

try:
    motor.active(0) 
    direction.value(1)
    motor.active(1)
    while True:
        utime.sleep(1)      # keeps the script alive; Ctrl+C / Stop lands here
except KeyboardInterrupt:
    pass
finally:
    motor.active(0)          # stop the PIO state machine
    motor.exec("set(pins, 0)")  # force STEP low
    direction.value(0)       # force DIR low
    print("Motor stopped")