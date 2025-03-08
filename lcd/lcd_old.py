# Hardware and connections used:
#   LCD GND Pin to Raspberry Pi Pico GND
#   LCD VCC Pin to Raspberry Pi Pico VBUS 
#   (Note: VBUS is only to be used as power for the screen. 
#   It can't be used as power for the entire circuit if there are other components interfaced.)
#   LCD SDA Pin to Raspberry Pi Pico GPIO Pin 0
#   LCD SCL Pin to Raspberry Pi Pico GPIO Pin 1
#
# Programmer: Adrian Josele G. Quional

# modules
from time import sleep

# very important
# this module needs to be saved in the Raspberry Pi Pico in order for the LCD I2C to be used 

    # input the pin numbers
        # creating an I2C object, specifying the data (SDA) and clock (SCL) pins used in the Raspberry Pi Pico
        # any SDA and SCL pins in the Raspberry Pi Pico can be used (check documentation for SDA and SCL pins)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# getting I2C address
I2C_ADDR = i2c.scan()[0]

# creating an LCD object using the I2C address and specifying number of rows and columns in the LCD
# LCD number of rows = 2, number of columns = 16
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# use pin1 and pin2 here? 
LED = Pin(15, Pin.OUT) 
BUTTON = Pin(16, Pin.IN)    # creating Push Button object, setting it as IN

str_pad = "_"
coinmsg = "Insert Coin" #0-10
startmsg = "Press button to start "
leng = len(startname) 
num = 16
credit = 1

def idle():
    while True: 
        if leng > 16:
            yay = startname[:num]
            num = num + 1
            lcd.putstr(startname)
            startname = startname + str_pad

while True:
    if credit == 0: 
        for i in range(0, 16+len(myString)):
            length = len(myString)
            pd = " "
            if i < 15:
                lcd.putstr(str_pad*(15-i))
                pd = i
            if i+1 > length:
                sliced = myString[i-length:]
                lcd.putstr(sliced)
                # lcd.putstr(str_pad * (15-len(sliced)-pd))
            else:
                lcd.putstr(myString[:i+1])
                # lcd.putstr(str_pad * (15-length-pd))

            lcd.putstr(" " * 16)
            # lcd.putstr(str_pad[i:])
            # lcd_text = myString[:i]
            # lcd.putstr(lcd_text)
            # # sleep(125)
            # lcd.putstr(str_pad)
    # if the signal from the button is HIGH (button is pressed), turn LED on
    else:
        lcd.putstr(idle)

        if BUTTON.value() == 1: 
            LED.on() 
            lcd.putstr("starting")
            sleep(5)        # "Hello world!" text would be displayed for 5 secs
            lcd.clear()
            sleep(1)  
   

    # otherwise, turn the LED off
        else:
            LED.off()

    # putstr method allows printing of the text in the LCD screen
    # for other methods that can be used, check lcd_api module
         # clear the text for 1 sec then print the text again
            
