from motors.motor import Motor
import time


motor_step_pin = 17
motor_dir_pin = 16

test_motor = Motor(motor_dir_pin, motor_step_pin)

print("MOVING")
test_motor.move(0)
time.sleep(1)
test_motor.stop()
print("STOPPED")