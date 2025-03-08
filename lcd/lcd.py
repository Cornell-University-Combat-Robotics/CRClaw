class Lcd:
    def __init__(self, gpio_pin, sda_pin,scl_pin,startmsg, playmsg, successmsg, failmsg):
        self.input_pin = gpio_pin
        self.start = startmsg
        self.gotcoin = playmsg
        self.success = successmsg
        self.fail = failmsg  
        i2c = I2C(0, sda=sda_pin, scl=scl_pin, freq=400000)

        # getting I2C address
        I2C_ADDR = i2c.scan()[0]

        # creating an LCD object using the I2C address and specifying number of rows and columns in the LCD
        # LCD number of rows = 2, number of columns = 16
        self.lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

    def print_intro(self):
        # print self.start to LCD screen         
        self.lcd.clear()
        self.lcd.putstr(self.startmsg)

    def print_got_coin(self):
        # print self.gotcoint to LCD screen
        self.lcd.clear()
        self.lcd.putstr(self.playmsg)

    def print_result(self, is_success):
        if is_success:
            # print self.success message
            self.lcd.clear()
            self.lcd.putstr(self.successmsg)
        else:
            # print self.fail message
            self.lcd.clear()
            self.lcd.putstr(self.failmsg)

    def reset(self):
        # clear the LCD screen
        self.lcd.clear()
