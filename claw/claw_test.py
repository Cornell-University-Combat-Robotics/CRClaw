from claw import Claw
import time

control_pin = 26

tester = Claw(control_pin)

while True:
    tester.update("clamp")
    time.sleep(3)
    
    tester.update("release")
    time.sleep(3)
