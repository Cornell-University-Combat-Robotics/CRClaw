from lcd_i2c import LCD
from machine import I2C, Pin
from time import sleep, ticks_ms, ticks_diff

# ---- SET UP ------
I2C_ADDR = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
FREQ = 800000

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=FREQ)
lcd = LCD(addr=I2C_ADDR, cols=I2C_NUM_COLS, rows=I2C_NUM_ROWS, i2c=i2c)
lcd.begin()
lcd.display()
lcd.clear()

# ---- MESSAGES ------
lcd_startmsg = "Insert 1 coin to start!"
lcd_playmsg = "The game has started!"
lcd_successmsg = "You are successful!"
lcd_failmsg = "You Failed. Try again with another coin."

# ---- FUNCTION DEFINITIONS ------
def scroll_message(lcd, message, row=0, duration=30, loop_delay=0.75, gap=2):
    width = lcd.cols
    
    # small gap between loops
    text = message + " " * gap
    text_len = len(text)

    start = ticks_ms()
    pos = 0

    while ticks_diff(ticks_ms(), start) < duration * 1000:
        window = ""

        for i in range(width):
            window += text[(pos + i) % text_len]

        lcd.set_cursor(0, row)
        lcd.print(window)

        pos = (pos + 1) % text_len
        sleep(loop_delay)

# ---- TEST CODE ------
scroll_message(lcd, lcd_startmsg, row=0, duration=10)
lcd.clear()

scroll_message(lcd, lcd_playmsg, row=0, duration=10)
lcd.clear()

scroll_message(lcd, lcd_successmsg, row=0, duration=10)
lcd.clear()

scroll_message(lcd, lcd_failmsg, row=0, duration=10)
lcd.clear()