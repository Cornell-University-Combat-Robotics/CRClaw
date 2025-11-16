from machine import Pin, Timer
import utime

dir_pin = Pin(16, Pin.OUT)
step_pin = Pin(17, Pin.OUT)
steps_per_revolution = 200

# Initialize timer
tim = Timer()

def step(t):
    global step_pin
    step_pin.value(not step_pin.value())

def rotate_motor(delay):
    # Set up timer for stepping
    tim.init(freq=1000000//delay, mode=Timer.PERIODIC, callback=step)

def loop():
    while True:
        print("Rotating clockwise slowly")
        # Set motor direction clockwise
        dir_pin.value(1)

        # Spin motor slowly
        rotate_motor(2000)
        utime.sleep_ms(steps_per_revolution)
        tim.deinit()  # stop the timer
        utime.sleep(1)
        print("Rotating counterclockwise quickly")

        # Set motor direction counterclockwise
        dir_pin.value(0)

        # Spin motor quickly
        rotate_motor(1000)
        utime.sleep_ms(steps_per_revolution)
        tim.deinit()  # stop the timer
        utime.sleep(1)

if __name__ == '__main__':
    loop()

# import utime
# dir_pin = Pin(16, Pin.OUT)
# step_pin = Pin(17, Pin.OUT)
# steps_per_revolution = 200
# # Initialize timer
# tim = Timer()
# def step(t):
#     global step_pin
#     step_pin.value(not step_pin.value())
# def rotate_motor(delay):
#     # Set up timer for stepping
#     tim.init(freq=1000000//delay, mode=Timer.PERIODIC, callback=step)
# def loop():
#     while True:
#         try:
#             # Set motor direction clockwise
#             # dir_pin.value(1)
#             # # Spin motor slowly
#             # rotate_motor(2000)
#             # utime.sleep_ms(steps_per_revolution)
#             # tim.deinit()  # stop the timer
#             # utime.sleep(1)
#             # Set motor direction counterclockwise
#             dir_pin.value(0)
#             # Spin motor quickly
#             rotate_motor(1000)
#             utime.sleep_ms(steps_per_revolution)
#             tim.deinit()  # stop the timer
#             utime.sleep(1)
#         except KeyboardInterrupt:
#             tim.deinit()
#             print("Motor stopped")
#             break
        
# if __name__ == '__main__':
#     loop()

###################################################################################################################

# import machine
# import math
# import time

# class Stepper:
#     def __init__(self,step_pin,dir_pin,en_pin=None,steps_per_rev=200,speed_sps=10,invert_dir=False,timer_id=-1):
        
#         if not isinstance(step_pin, machine.Pin):
#             step_pin=machine.Pin(step_pin,machine.Pin.OUT)
#         if not isinstance(dir_pin, machine.Pin):
#             dir_pin=machine.Pin(dir_pin,machine.Pin.OUT)
#         if (en_pin != None) and (not isinstance(en_pin, machine.Pin)):
#             en_pin=machine.Pin(en_pin,machine.Pin.OUT)
                 
#         self.step_value_func = step_pin.value
#         self.dir_value_func = dir_pin.value
#         self.en_pin = en_pin
#         self.invert_dir = invert_dir

#         self.timer = machine.Timer(timer_id)
#         self.timer_is_running=False
#         self.free_run_mode=0
#         self.enabled=True
        
#         self.target_pos = 0
#         self.pos = 0
#         self.steps_per_sec = speed_sps
#         self.steps_per_rev = steps_per_rev
        
#         self.track_target()
        
#     def speed(self,sps):
#         self.steps_per_sec = sps
#         if self.timer_is_running:
#             self.track_target()
    
#     def speed_rps(self,rps):
#         self.speed(rps*self.steps_per_rev)

#     def target(self,t):
#         self.target_pos = t

#     def target_deg(self,deg):
#         self.target(self.steps_per_rev*deg/360.0)
    
#     def target_rad(self,rad):
#         self.target(self.steps_per_rev*rad/(2.0*math.pi))
    
#     def get_pos(self):
#         return self.pos
    
#     def get_pos_deg(self):
#         return self.get_pos()*360.0/self.steps_per_rev
    
#     def get_pos_rad(self):
#         return self.get_pos()*(2.0*math.pi)/self.steps_per_rev
    
#     def overwrite_pos(self,p):
#         self.pos = 0
    
#     def overwrite_pos_deg(self,deg):
#         self.overwrite_pos(deg*self.steps_per_rev/360.0)
    
#     def overwrite_pos_rad(self,rad):
#         self.overwrite_pos(rad*self.steps_per_rev/(2.0*math.pi))

#     def step(self,d):
#         if d>0:
#             if self.enabled:
#                 self.dir_value_func(1^self.invert_dir)
#                 self.step_value_func(1)
#                 self.step_value_func(0)
#             self.pos+=1
#         elif d<0:
#             if self.enabled:
#                 self.dir_value_func(0^self.invert_dir)
#                 self.step_value_func(1)
#                 self.step_value_func(0)
#             self.pos-=1

#     def _timer_callback(self,t):
#         if self.free_run_mode>0:
#             self.step(1)
#         elif self.free_run_mode<0:
#             self.step(-1)
#         elif self.target_pos>self.pos:
#             self.step(1)
#         elif self.target_pos<self.pos:
#             self.step(-1)
    
#     def free_run(self,d):
#         self.free_run_mode=d
#         if self.timer_is_running:
#             self.timer.deinit()
#         if d!=0:
#             self.timer.init(freq=self.steps_per_sec,callback=self._timer_callback)
#             self.timer_is_running=True
#         else:
#             self.dir_value_func(0)

#     def track_target(self):
#         self.free_run_mode=0
#         if self.timer_is_running:
#             self.timer.deinit()
#         self.timer.init(freq=self.steps_per_sec,callback=self._timer_callback)
#         self.timer_is_running=True

#     def stop(self):
#         self.free_run_mode=0
#         if self.timer_is_running:
#             self.timer.deinit()
#         self.timer_is_running=False
#         self.dir_value_func(0)

#     def enable(self,e):
#         if self.en_pin:
#             self.en_pin.value(e)
#         self.enabled=e
#         if not e:
#             self.dir_value_func(0)
    
#     def is_enabled(self):
#         return self.enabled



# s2 = Stepper(6,7,steps_per_rev=200,speed_sps=10)
# print("Running", s2.is_enabled())
# s2.free_run(1)
# while True:
#     try:
#         time.sleep(1)
#         print("Position:",s2.get_pos())
#     except KeyboardInterrupt:
#         print("Stopping")
#         s2.stop()
#         break

###################################################################################################################

# from machine import Pin, Timer
# from time import sleep_ms

# class DRV8825(object):
#     """ Class to control a bi-polar stepper motor with a DRV8825 """

#     # dictionary with microstepping settings of pins (M0, M1, M2)
#     microstep_dict = {
#                         1 : (0, 0, 0),
#                         2 : (1, 0, 0),
#                         4 : (0, 1, 0),
#                         8 : (1, 1, 0),
#                        16 : (0, 0, 1),
#                        32 : (1, 0, 1)
#                      }

#     def __init__(self,
#                  step_pin,
#                  direction_pin=None,
#                  microstep_pins=None,
#                  sleep_pin=None,
#                  reset_pin=None,
#                  timer_id=-1,
#                  steps_per_revolution=200):
#         """
#         <step_pin>  (number) pin connected to STEP of DRV8825
#         <direction_pin> (number) pin connected to DIR of DRV8825
#         <microstep_pins> (tuple) 3 pins connected to M0,M1,M2 of DRV8825
#                     for microstep resolution.
#         <sleep_pin> (number) pin connected to SLEEP of DRV8825
#         <reset_pin> (number) pin connected to RESET of DRV8825
#         <timer_id>  (number) timer to use for step timing, the default
#                     value -1 (last timer) usually works on most boards
#         <steps_per_revolution> (number) Full steps for 360 degrees revolution
#         Notes: - <step_pin> is mandatory.
#                - other pins are optional (presumably fixed wired)
#                - instances of DRV8825 are started enabled.
#         """
#         self._step_pin = Pin(step_pin, Pin.OUT)
#         self._direction_pin = None
#         if direction_pin is not None:
#             self._direction_pin = Pin(direction_pin, Pin.OUT)
#         self._microstep_pins = None
#         if microstep_pins is not None:
#             if len(microstep_pins) == 3:
#                 self._microstep_pins = [Pin(p, Pin.OUT) for p in microstep_pins]
#             else:
#                 print("microstep_pins must be specified as tuple of 3 numbers")
#         self._sleep_pin = None
#         if sleep_pin is not None:
#             self._sleep_pin = Pin(sleep_pin, Pin.OUT)
#         self._reset_pin = None
#         if reset_pin is not None:
#             self._reset_pin = Pin(reset_pin, Pin.OUT)
#         self.steps_per_revolution = steps_per_revolution    # full steps for 360 degrees
#         self._timer = Timer(timer_id, mode=Timer.PERIODIC)  # interval timer for stepping
#         self._timer_running = False             # timer is not running yet
#         self._free_run_mode = 0                 # not running free
#         self._actual_pos = 0                    # actual position
#         self._target_pos = 0                    # target position

#     def enable(self):
#         """ Enable the DRV8825
#             When pins for sleep and reset are not specified
#             reset and sleep pins must be pulled high externally,
#             Enable pin may be left unconnected or must be pulled
#             low externally.
#         """
#         if self._sleep_pin is not None:
#             self._sleep_pin.on()                # wake up
#         if self._reset_pin is not None:
#             self._reset_pin.on()                # leave reset state
#         sleep_ms(3)                             # datasheet: minimum 1.7 ms

#     def disable(self):
#         """ Disable the DRV8825 """
#         self.stop()                             # stop stepping
#         if self._sleep_pin is not None:
#             self._sleep_pin.off()               # put asleep
#         if self._reset_pin is not None:
#             self._reset_pin.off()               # enter reset state

#     def reset(self, state=True, interval=None):
#         """ Reset the DRV8825 (True) or undo previous reset (False)
#             When interval (milliseconds) is specified
#             the DRV8825 is reset pin for the specified
#             time and then re-activated.
#             Reset pin must have been specified with object creation.
#         """
#         if self._reset_pin is not None:         # reset pin is specified
#             if interval is not None:            # interval specified
#                 self._reset_pin.off()
#                 sleep_ms(interval)              # milliseconds
#                 self._reset_pin.on()
#             else:
#                 self._reset_pin.value(state)    # negative logic

#     def stop(self):
#         """ Stop stepping, but keep motor enabled (in position),
#             it prevents for example bouncing back from an endswitch.
#         """
#         self._timer.deinit()                    # (running or not)
#         self._timer_running = False

#     def resolution(self, microsteps=1):
#         """ method to set step number of microsteps per full step
#             <microsteps> supported values: 1,2,4,8,16,32
#         """
#         if self._microstep_pins is not None:
#             microstep = __class__.microstep_dict.get(microsteps, (0,0,0))
#             for i in range(3):
#                 self._microstep_pins[i].value(microstep[i])
#             # print("M0,M1,M2: ", ",".join(["{:d}"
#             #      .format(self._microstep_pins[m].value()) for m in range(3)]))
#         return microsteps

#     def one_step(self, direction):
#         """ perform one step (forward if direction > 0, backward if direction < 0)
#         """
#         if direction > 0:
#             self._direction_pin.on()
#             self._step_pin.on()                 # actual step (rising edge)
#             self._actual_pos += 1
#             self._step_pin.off()
#         elif direction < 0:
#             self._direction_pin.off()
#             self._step_pin.on()
#             self._actual_pos -= 1
#             self._step_pin.off()

#     def _timer_callback(self, t):
#         """ determine if stepping action opportune
#             if true perform one step forward or backward
#         """
#         if self._free_run_mode != 0:
#             self.one_step(1 if self._free_run_mode > 0 else -1)
#         elif self._target_pos != self._actual_pos:  # target not reached yet
#             self.one_step(1 if self._target_pos > self._actual_pos else -1)

#     def steps(self, steps, microsteps=1, stepfreq=200):
#         """  move stepper motor a number of steps:
#              <steps> (number)
#                      Number of steps to take.
#                      Positive number: clockwise, negative: counter clockwise
#              <microsteps> (integer)
#                      Supported values 1,2,4,8,16,32
#              <stepfreq> (number)
#                      step frequency: (micro-)steps per second (Hz)
#         """
#         self.resolution(microsteps)             # microstepping (?)
#         self.enable()                           # enable drv8825 hardware
#         self._free_run_mode = 0
#         self._actual_pos = 0                    # new starting point
#         self._target_pos = steps                # new target (pos/neg)
#         self._timer.init(freq=abs(stepfreq), callback=self._timer_callback)
#         self._timer_running = True

#     def revolutions(self, revolutions, microsteps=1, stepfreq=200):
#         """  move stepper motor a number of full revolutions:
#              <revolutions> (number)
#                      Number of full (360 degrees) revolutions.
#                      Positive number: clockwise, negative: counter clockwise
#              <microsteps> (integer)
#                      Supported values: 1,2,4,8,16,32
#              <stepfreq> (number)
#                      step frequency: steps per second (Hz)
#         """
#         if microsteps not in __class__.microstep_dict:
#             print("Supported microsteps: 1,2,4,8,16,32")
#             microsteps = 1
#         steps = revolutions * self.steps_per_revolution * microsteps
#         self.steps(steps, microsteps, stepfreq)

#     def freerun(self, stepfreq=200, microsteps=1):
#         """  keep stepper motor stepping indefinitely
#              (until stopped explicitly)
#              <stepfreq> (number)
#                      step frequency: steps per second (Hz)
#                      positive value: forward, negative: backward
#              <microsteps> (integer)
#                      Supported values: 1,2,4,8,16,32
#         """
#         self._timer.deinit()                # disable timer
#         self._timer_running = False
#         if stepfreq == 0:                   # motor stopped
#             return
#         self.enable()                       # enable drv8825 hardware
#         self.resolution(microsteps)
#         self._free_run_mode = 1 if stepfreq > 0 else -1     # forward/backward
#         self._timer.init(freq=abs(stepfreq), callback=self._timer_callback)
#         self._timer_running = True
#         return

#     def get_progress(self):
#         """ getter method
#             return steps taken so far to reach target (negative with CCW!)
#         """
#         if self._free_run_mode != 0:        # free running
#             return 0                        # what else to say?
#         return self._actual_pos             # steps taken in 'this' operation


# motor = DRV8825(step_pin=6, direction_pin=7)
# motor.freerun()
# while True:
#     try:
#         motor.steps(10)
#         sleep_ms(1000)
#         print("Steps taken:", motor.get_progress())
#     except KeyboardInterrupt:
#         motor.stop()
#         print("Stopping motor")
#         break


###################################################################################################################

# from time import sleep
# from machine import Pin

# # PINs (alter to be accurate)
# DIR = Pin(22, Pin.OUT) # direction GPIO pin
# STEP = Pin(21, Pin.OUT) # step GPIO pin
# CW = 1 # clockwise
# CCW = 0 # counterclockwise
# SPR = 8000 # steps per revolution (360 / 7.5 = 48 so we're turning 7.5 degrees per revolution)

# # Note, like we did in autonmous, we may have to switch to hardware pwm (pigpio instead of RPi.GPIO)

# DIR.value(CW)  # sets initial direction to clockwise

# step_count = SPR
# delay = .008

# # for like 2 seconds, we pulse the motor to rotate clockwise
# print("Rotating clockwise...")
# for x in range(step_count):
#     STEP.value(1)
#     sleep(delay)
#     STEP.value(0)
#     sleep(delay)


# sleep(.5)
# DIR.value(CCW) # now we go counter clockwise
# print("Rotating counter clockwise...")
# for x in range(step_count):
#     STEP.value(1)
#     sleep(delay)
#     STEP.value(0)
#     sleep(delay)
