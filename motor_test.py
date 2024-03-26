from time import sleep
import RPi.GPIO as GPIO # this gives us access to the pi pins

# PINs (alter to be accurate)
DIR = 20 # direction GPIO pin
STEP = 21 # step GPIO pin


CW = 1 # clockwise
CCW = 0 # counterclockwise
SPR = 48 # steps per revolution (360 / 7.5 = 48 so we're turning 7.5 degrees per revolution)

# Note, like we did in autonmous, we may have to switch to hardware pwm (pigpio instead of RPi.GPIO)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)  # sets initial direction to clockwise

delay = .00000008

try: 
    print("Running Motor")
    while True:
        GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        GPIO.output(STEP, GPIO.LOW)
        sleep(delay)
        print("Running")

except KeyboardInterrupt:
    GPIO.cleanup()
    print("died")



# step_count = SPR
# delay = .0208


# # for like 2 seconds, we pulse the motor to rotate clockwise
# for x in range(step_count):
#     GPIO.output(STEP, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP, GPIO.LOW)
#     sleep(delay)

# sleep(.5)
# GPIO.output(DIR, CCW) # now we go counter clockwise

# for x in range(step_count):
#     GPIO.output(STEP, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP, GPIO.LOW)
#     sleep(delay)