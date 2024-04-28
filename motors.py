from time import sleep
import RPi
import RPi.GPIO as GPIO # this gives us access to the pi pins

# PINs (alter to be accurate)
DIR = 20 # direction GPIO pin
STEP = 21 # step GPIO pin

class Motor():
    CW = 1 # clockwise
    CCW = 0 # counterclockwise
    SPR = 8000 # steps per revolution (360 / 7.5 = 48 so we're turning 7.5 degrees per revolution)

    # Note, like we did in autonmous, we may have to switch to hardware pwm (pigpio instead of RPi.GPIO)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, CW)  # sets initial direction to clockwise

    step_count = SPR
    delay = .0008
    #joy_inputs: left, right, front (close), back(far) 
    #switch_inputs: 
    #joy_inputs list of all joystick directions (booleans) that are being pressed (true)

    def __init__(self, step_pin):
        self.step_pin = step_pin
        
    
    # NOTE: doesn't check if hit limit switch
    # direction is CW or CCW 
    def move(self, direction, steps = 1): 
        # move (increment step) in direction
        if(steps > 1):
            for step in range(steps):
                GPIO.output(Motor.DIR, direction)
                GPIO.output(Motor.STEP, GPIO.HIGH)
                sleep(Motor.delay)
                GPIO.output(Motor.STEP, GPIO.LOW)
                sleep(Motor.delay)
            print("moved")
        else:
            # one step
            GPIO.output(Motor.DIR, direction)
            GPIO.output(Motor.STEP, GPIO.HIGH)
            sleep(Motor.delay)
            GPIO.output(Motor.STEP, GPIO.LOW)
            sleep(Motor.delay)

    def stop(self):
        GPIO.output(Motor.DIRÍ)
        sleep(Motor.delay)
        GPIO.output(0, GPIO.HIGH)

    def cleanup(self):
        GPIO.cleanup

    