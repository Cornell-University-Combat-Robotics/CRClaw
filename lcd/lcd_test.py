from lcd_i2c import LCD
from machine import I2C, Pin
import time

lcd_startmsg = "Insert 1 Coin to Start"
lcd_playmsg = "The Game has Started"
lcd_successmsg = "You are Successful!"
lcd_failmsg = "You Failed. Try again with Another Coin"


i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=800000)
lcd = LCD(addr=0x27, cols=4, rows=20, i2c=i2c)
lcd.display()

lcd.print(lcd_startmsg)
time.sleep(1.0)
lcd.clear()

lcd.print(lcd_playmsg)
time.sleep(1.0)
lcd.clear()

lcd.print(lcd_successmsg)
time.sleep(1.0)
lcd.clear()

lcd.print(lcd_failmsg)
time.sleep(1.0)
lcd.clear()