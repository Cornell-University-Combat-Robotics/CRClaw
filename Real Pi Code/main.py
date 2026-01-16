from machine import Pin, Timer
import utime

dir_pin = Pin(16, Pin.OUT)
step_pin = Pin(17, Pin.OUT)
steps_per_revolution = 2000

# Initialize timer
tim = Timer()

def step(t):
    global step_pin
    step_pin.value(not step_pin.value())

def rotate_motor(delay):
    # Set up timer for stepping 10 ->5
    tim.init(freq=1000000//delay, mode=Timer.PERIODIC, callback=step)

def loop():
    try:
        while True:
            for i in range(560, 570, 3): # even and odd number and inbetween ccw cw and jerking 
                print(f"Trying delay = {i}")
                print("spinning clockwise") # the clock wise and counter depended on increments 
                # Set motor direction clockwise
                dir_pin.value(1)

                # Spin motor slowly
                rotate_motor(i)
                utime.sleep_ms(steps_per_revolution)
                tim.deinit()  # stop the timer
                utime.sleep(3)

#                 print("spinning counterclockwise")
#                 # Set motor direction counterclockwise
#                 dir_pin.value(0)
# 
#                 # Spin motor quickly
#                 rotate_motor(i)
#                 utime.sleep_ms(steps_per_revolution)
#                 tim.deinit()  # stop the timer
#                 utime.sleep(1)
    except:
        print("turning off")
        tim.deinit()  # stop the timer
        utime.sleep(1)
if __name__ == '__main__':
    loop()
