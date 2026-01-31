"""

TODO: 
Thing we need in this file
✓ adapt lcd code in here for class (move file to this branch)
- adapt code for coin sensor class (lowkey needs be threading)
✓ adapt for limit switch class
✓ remove music/speaker
✓ Remove chute sensor
✓ adapt to button class
✓ adapt to joystick class
✓ adapt to claw class
-- Initialize motors correctly?

Things we need to do in other files
✓ Make class for limit switches
✓ make class for button
✓ make joystick class
✓ make class for claw
- Need motor class (side lining)
-- edit claw class to support lowering


"""

from button.button import Button
from claw.claw import Claw
from joystick.joystick import Joystick
from motors.motor import Motor
from sensors.sensor import Sensor
from switch.switch import Switch

from lcd_i2c import LCD
from machine import I2C, Pin


# ------------------------ Constants ------------------------

# TODO: Subject to change for testing
NEG = -1
ZERO = 0
POS = 1
lcd_startmsg = "Insert 1 Coin to Start"
lcd_playmsg = "The Game has Started"
lcd_successmsg = "You are Successful!"
lcd_failmsg = "You Failed. Try again with Another Coin"

# ------------------------ GPIO Pins ------------------------

# TODO: Subject to change for testing
lcd_sda_pin = 20 
lcd_scl_pin = 21
button_gpio_pin = 2 # FIX Pin number
joystick_f_switch_pin = 5
joystick_b_switch_pin = 4
joystick_l_switch_pin = 3
joystick_r_switch_pin = 2
boundary_lswitch_pin = 7 # FIX
boundary_rswitch_pin = 8 # FIX
boundary_fswitch_pin = 9 # FIX
boundary_bswitch_pin = 10 # FIX
claw_motor_pin = 12 # FIX
claw_close_pin = 13 # FIX
coin_sensor_pin = 10

# -----------------------------------------------------------

# repeatedly loops round() to allow for repeated games
def main():
    coin_sensor = Sensor(pin=coin_sensor_pin, sensor_type="coin")
    i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=800000)
    lcd = LCD(addr=0x27, cols=4, rows=20, i2c=i2c)
    
    button = Button(button_gpio_pin)

    fbmotor = Motor()  # TODO: correctly initialize
    lrmotor = Motor()  # TODO: correctly initialize
    motors = [fbmotor, lrmotor]

    claw = Claw(claw_motor_pin, claw_close_pin)
    joystick = Joystick(
        joystick_f_switch_pin,
        joystick_b_switch_pin,
        joystick_l_switch_pin,
        joystick_r_switch_pin,
    )

    end_fswitch = Switch(boundary_fswitch_pin)
    end_bswitch = Switch(boundary_bswitch_pin)
    end_lswitch = Switch(boundary_lswitch_pin)
    end_rswitch = Switch(boundary_rswitch_pin)
    end_switches = [end_fswitch, end_bswitch, end_lswitch, end_rswitch]

    while True:
        lcd.print(lcd_startmsg)
        round(coin_sensor, lcd, button, motors, claw, joystick, end_switches)

# resets the game
def reset(lcd):
    lcd.clear()

# Contains logic for one round of the game. Processes a coin insertion (which begins the game),
# button presses, joystick movement, and game duration.
def round(
    coin_sensor: Sensor,
    lcd: LCD,
    button: Button,
    motors: list[Motor],
    claw: Claw,
    joystick: Joystick,
    end_switches: list[Switch],
):
    while True:
        if coin_sensor.detected():
            lcd.print(lcd_playmsg)
            break

    while True:
        # game over or pressed button
        if button.is_pressed():
            motors.go_down()
            claw.clamp()
            motors.go_up()
            motors.reset()
            claw.release()

            lcd.print(lcd_successmsg) # just make default game over message cause we dont know if its a success

            reset()
            break

        # poll joystick movement, if joystick is at edge, only move if it is moving the opposite way
        else:
            direction = joystick.update()  # converts FBRL array to a length 2 array
            # at left end
            if end_switches[1].is_touched():
                motors[0].move(direction.get(0))  # fbmotor1
                if direction.get(1) == POS:  # or NEG, idk, whichever is right
                    motors[1].move(direction.get(1))  # lrmotor

            # at right end
            elif end_switches[3].is_touched():
                motors[0].move(direction.get(0))  # fbmotor1
                if direction.get(1) == NEG:  # or POS, idk, whichever is left
                    motors[1].move(direction.get(1))  # lrmotor

            # at front end
            elif end_switches[0].is_touched():
                motors[1].move(direction.get(1))  # lrmotor
                if direction.get(0) == POS:
                    motors[0].move(direction.get(0))  # fbmotor1
            
            # at back end
            elif end_switches[1].is_touched():
                motors[1].move(direction.get(1))  # lrmotor
                if direction.get(0) == NEG:
                    motors[0].move(direction.get(0))  # fbmotor

            else:  # move as usual
                motors[0].move(direction.get(0))  # fbmotor
                motors[1].move(direction.get(1))  # lrmotor