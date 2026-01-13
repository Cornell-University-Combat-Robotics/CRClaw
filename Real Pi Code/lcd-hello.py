"""
This Raspberry Pi Pico MicroPython code was developed by newbiely.com
This Raspberry Pi Pico code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-lcd-20x4
"""

from machine import I2C, Pin
from DIYables_MicroPython_LCD_I2C import LCD_I2C
import utime

# The I2C address of your LCD (Update if different)
I2C_ADDR = 0x27  # Use the address found using the I2C scanner

# Define the number of rows and columns on your LCD
LCD_COLS = 20
LCD_ROWS = 4

# Initialize I2C
i2c = I2C(0, sda=Pin(6), scl=Pin(7), freq=400000)

# Initialize LCD
lcd = LCD_I2C(i2c, I2C_ADDR, LCD_ROWS, LCD_COLS)

# Setup function
lcd.backlight_on()
lcd.clear()

# Main loop function
while True:
    lcd.clear()
    lcd.set_cursor(0, 0);            # Move cursor at the first row, first column
    lcd.print("LCD 20x4");           # Display text at the first row
    lcd.set_cursor(0, 1);            # Move cursor at the second row, first column
    lcd.print("I2C Address: 0x27");  # Display text at the second row
    lcd.set_cursor(0, 2);            # Move cursor at the third row, first column
    lcd.print("DIYables");           # Display text at the third row
    lcd.set_cursor(0, 3);            # Move cursor at the fourth row, first column
    lcd.print("www.diyables.io");    # Display text at the fourth row
    utime.sleep(2)
    
    lcd.clear()
    lcd.set_cursor(0, 0) # Move to the beginning of the first row
    lcd.print("Int: ")
    lcd.print(str(197))  # Print integer
    lcd.set_cursor(0, 1)  # Move to the beginning of the second row
    lcd.print("Float: ")
    lcd.print(str(26.39))  # Print float
    utime.sleep(2)
