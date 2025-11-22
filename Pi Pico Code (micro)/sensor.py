from machine import Pin
import utime

class Sensor:
    def __init__(self, pin, sensor_type):
        self.sensor_type = sensor_type # Either "coin" or "chute"
        self.state = False  # default state (false for no coin/toy detected)
        self.num_coins_detected = 0

        self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)

    def detected(self):
        new_state = self.pin.value()
        if new_state == 0 and self.state == 1:
            # self.state = True
            # if self.sensor_type == "coin":
            #     print("Coin detected!")
            # elif self.sensor_type == "chute":
            #     print("Toy detected in the chute!")
            self.state = new_state
            self.num_coins_detected += 1
            print ("Coins seen: ", self.num_coins_detected)
        elif new_state == 1 and self.state == 0:
            # self.state = False
            self.state = new_state

    def get_coins(self):
        return self.num_coins_detected

    def reset(self):
        self.pin.low()
        self.num_coins_detected = 0
        self.state = False

    # def gpio_cleanup(self):
    #     GPIO.cleanup()
        
if __name__ == "__main__":
    coin_sensor = Sensor(pin="GP10", sensor_type="coin")
    #chute_sensor = Sensor(pin="GPIO10", sensor_type="chute")
    print ("Coin Sensor started")
    while (True):
        coin_sensor.detected()
    # if chute_sensor.detected():
    #     print("Toy collected successfully!")
    
    # coin_sensor.reset()
    # chute_sensor.reset()

    # coin_sensor.cleanup()
    # chute_sensor.cleanup()
    