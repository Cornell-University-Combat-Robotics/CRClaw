from button.button import Button
from claw.claw import Claw
from joystick.joystick import Joystick
from lcd.lcd_sudo import Lcd
from motors.motor import Motor
from sensors.sensor import Sensor
from switch.switch import Switch
from music.music import Music

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
lcd_gpio_pin = 1
button_gpio_pin = 2
joystick_f_switch_pin = 3
joystick_b_switch_pin = 4
joystick_l_switch_pin = 5
joystick_r_switch_pin = 6
boundary_lswitch_pin = 7
boundary_rswitch_pin = 8
boundary_fswitch_pin = 9
boundary_bswitch_pin = 10

# -----------------------------------------------------------

# repeatedly loops round() to allow for repeated games
def main():
    coin_sensor = Sensor(pin=11, sensor_type="coin")
    chute_sensor = Sensor(pin=12, sensor_type="chute")

    lcd = Lcd(lcd_gpio_pin, lcd_startmsg, lcd_playmsg, lcd_successmsg, lcd_failmsg)
    button = Button(button_gpio_pin)

    fbmotor1 = Motor()  # TODO: correctly initialize
    fbmotor2 = Motor()  # TODO: correctly initialize
    lrmotor = Motor()  # TODO: correctly initialize
    motors = [fbmotor1, fbmotor2, lrmotor]

    claw = Claw()  # TODO: correctly initialize
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

    music = Music("music.mp3")

    while True:
        lcd.print_intro()
        round(coin_sensor, chute_sensor, lcd, button, motors, claw, joystick, end_switches, music)

# resets the game
def reset(music, lcd):
    music.end_music()
    lcd.reset()

# Contains logic for one round of the game. Processes a coin insertion (which begins the game),
# button presses, joystick movement, and game duration.
def round(
    coin_sensor: Sensor,
    chute_sensor: Sensor,
    lcd: Lcd,
    button: Button,
    motors: list[Motor],
    claw: Claw,
    joystick: Joystick,
    end_switches: list[Switch],
    music: Music
):
    while True:
        if coin_sensor.detected():
            lcd.print_got_coin()
            music.start_music()
            break

    while True:
        # game over or pressed button
        if button.is_pressed() or not music.is_music_playing:
            motors.go_down()
            claw.clamp()
            motors.go_up()
            motors.reset()
            claw.release()

            is_toy = chute_sensor.detected()
            lcd.is_success(is_toy)

            reset()
            break

        # poll joystick movement, if joystick is at edge, only move if it is moving the opposite way
        else:
            direction = joystick.update()  # converts FBRL array to a length 2 array
            # at left end
            if end_switches[2].is_touched():
                motors[0].move(direction.get(0))  # fbmotor1
                motors[1].move(direction.get(0))  # fbmotor2
                if direction.get(1) == POS:  # or NEG, idk, whichever is right
                    motors[2].move(direction.get(1))  # lrmotor

            # at right end
            elif end_switches[3].is_touched():
                motors[0].move(direction.get(0))  # fbmotor1
                motors[1].move(direction.get(0))  # fbmotor2
                if direction.get(1) == NEG:  # or POS, idk, whichever is left
                    motors[2].move(direction.get(1))  # lrmotor

            # at front end
            elif end_switches[0].is_touched():
                motors[2].move(direction.get(1))  # lrmotor
                if direction.get(0) == POS:
                    motors[0].move(direction.get(0))  # fbmotor1
                    motors[1].move(direction.get(0))  # fbmotor2
            # at back end
            elif end_switches[1].is_touched():
                motors[2].move(direction.get(1))  # lrmotor
                if direction.get(0) == NEG:
                    motors[0].move(direction.get(0))  # fbmotor1
                    motors[1].move(direction.get(0))  # fbmotor2
            else:  # move as usual
                motors[0].move(direction.get(0))  # fbmotor1
                motors[2].move(direction.get(1))  # lrmotor
                motors[1].move(direction.get(0))  # fbmotor2