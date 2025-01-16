from time import sleep
import RPi
import RPi.GPIO as GPIO # this gives us access to the pi pins



class Motor():
    # PINs (alter to be accurate)
    CW = 1 # clockwise
    CCW = 0 # counterclockwise
    SPR = 8000 # steps per revolution (360 / 7.5 = 48 so we're turning 7.5 degrees per revolution)
    step_count = SPR
    delay = .0008
    # Note, like we did in autonmous, we may have to switch to hardware pwm (pigpio instead of RPi.GPIO)

    #joy_inputs: left, right, front (close), back(far) 
    #switch_inputs: 
    #joy_inputs list of all joystick directions (booleans) that are being pressed (true)

    def __init__(self, step_pin, dir_pin):
        self.step_pin = step_pin
        self.dir_pin = dir_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(dir_pin, GPIO.OUT)
        GPIO.setup(step_pin, GPIO.OUT)
        GPIO.output(dir_pin, Motor.CW)  # sets initial direction to clockwise
        
    # NOTE: doesn't check if hit limit switch
    # direction is CW or CCW 
    def move(self, direction, steps = 1): 
        # move (increment step) in direction
        if(steps > 1):
            for step in range(steps):
                GPIO.output(self.dir_pin, direction)
                GPIO.output(self.step_pin, GPIO.HIGH)
                sleep(Motor.delay)
                GPIO.output(self.step_pin, GPIO.LOW)
                sleep(Motor.delay)
            print("moved")
        else:
            # one step
            GPIO.output(self.dir_pin, direction)
            GPIO.output(self.step_pin, GPIO.HIGH)
            sleep(Motor.delay)
            GPIO.output(self.step_pin, GPIO.LOW)
            sleep(Motor.delay)

    def stop(self):
        GPIO.output(self.dir_pin)
        sleep(Motor.delay)
        GPIO.output(0, GPIO.HIGH)
        print("stop")

    def cleanup(self):
        GPIO.cleanup

    