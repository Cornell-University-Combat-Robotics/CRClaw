import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, gpio_pin, sensor_type):
        self.gpio_pin = gpio_pin
        self.sensor_type = sensor_type # Either "coin" or "chute"
        self.state = False  # default state (false for no coin/toy detected)
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def detected(self):
        if GPIO.input(self.pin) == GPIO.HIGH:
            self.state = True
            if self.sensor_type == "coin":
                print("Coin detected!")
            elif self.sensor_type == "chute":
                print("Toy detected in the chute!")
            return True
        else:
            self.state = False
            return False

    def reset(self):
        GPIO.input(self.pin) == GPIO.LOW
        self.state = False

    def gpio_cleanup(self):
        GPIO.cleanup()
        
if __name__ == "__main__":
    coin_sensor = Sensor(pin=11, sensor_type="coin")
    chute_sensor = Sensor(pin=12, sensor_type="chute")
    
    if coin_sensor.detected():
        print("Coin detected. Ready to operate the claw!")
    
    if chute_sensor.detected():
        print("Toy collected successfully!")
    
    coin_sensor.reset()
    chute_sensor.reset()

    coin_sensor.cleanup()
    chute_sensor.cleanup()