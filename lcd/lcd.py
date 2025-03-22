import smbus2 as smbus
import time

class Lcd():
    """
    A class to interface with a 16x4 (or larger) I2C LCD display.

    This class provides methods to send commands and data to an LCD screen using 
    the I2C protocol, allowing for text display with customizable alignment.

    Attributes
    ----------
    I2C_ADDR : int
        The I2C device address for the LCD. Defaults to 0x27.
    LCD_WIDTH : int
        The maximum number of characters per line. Defaults to 16.
    LCD_CHR : int
        Mode identifier for sending data to the LCD.
    LCD_CMD : int
        Mode identifier for sending commands to the LCD.
    LCD_LINE_1 : int
        Memory address for the first line of the LCD.
    LCD_LINE_2 : int
        Memory address for the second line of the LCD.
    LCD_LINE_3 : int
        Memory address for the third line of the LCD.
    LCD_LINE_4 : int
        Memory address for the fourth line of the LCD.
    LCD_BACKLIGHT : int
        Flag to enable the LCD backlight.
    ENABLE : int
        Enable bit used for toggling commands.
    E_PULSE : float
        Pulse time for enable signal.
    E_DELAY : float
        Delay time for enable signal stabilization.
    bus : smbus.SMBus
        The I2C bus object used to communicate with the LCD.

    Methods
    -------
    __init__()
        Initializes the LCD display with default settings.
    lcd_byte(bits, mode)
        Sends a byte of data or command to the LCD.
    lcd_toggle_enable(bits)
        Toggles the enable bit to process a command or data byte.
    lcd_string(message, line, align="left")
        Displays a message on a specified line of the LCD with the given alignment.

    Notes
    -----
    - This class is designed for use with Raspberry Pi devices that support I2C.
    - If the display is not responding, the I2C address (I2C_ADDR) may need to be adjusted.
    - Only the first `LCD_WIDTH` characters of a message will be displayed per line.
    """



    # Define some device parameters
    I2C_ADDR = 0x27     # I2C device address, if any error, change this address to 0x3f
    LCD_WIDTH = 16      # Maximum characters per line

    # Define some device constants
    LCD_CHR = 1     # Mode - Sending data
    LCD_CMD = 0     # Mode - Sending command

    LCD_LINE_1 = 0x80   # LCD RAM address for the 1st line
    LCD_LINE_2 = 0xC0   # LCD RAM address for the 2nd line
    LCD_LINE_3 = 0x94   # LCD RAM address for the 3rd line
    LCD_LINE_4 = 0xD4   # LCD RAM address for the 4th line

    LCD_BACKLIGHT = 0x08  # On

    ENABLE = 0b00000100     # Enable bit

    # Timing constants
    E_PULSE = 0.0005
    E_DELAY = 0.0005

    # Open I2C interface
    # bus = smbus.SMBus(0)  # Rev 1 Pi uses 0
    bus = smbus.SMBus(1)    # Rev 2 Pi uses 1


    def __init__(self):
        # Initialise display
        self.lcd_byte(0x33, Lcd.LCD_CMD)     # 110011 Initialise
        self.lcd_byte(0x32, Lcd.LCD_CMD)     # 110010 Initialise
        self.lcd_byte(0x06, Lcd.LCD_CMD)     # 000110 Cursor move direction
        self.lcd_byte(0x0C, Lcd.LCD_CMD)     # 001100 Display On,Cursor Off, Blink Off
        self.lcd_byte(0x28, Lcd.LCD_CMD)     # 101000 Data length, number of lines, font size
        self.lcd_byte(0x01, Lcd.LCD_CMD)     # 000001 Clear display
        time.sleep(Lcd.E_DELAY)


    def lcd_byte(self, bits, mode):
        # Send byte to data pins
        # bits = the data
        # mode = 1 for data
        #        0 for command

        bits_high = mode | (bits & 0xF0) | Lcd.LCD_BACKLIGHT
        bits_low = mode | ((bits << 4) & 0xF0) | Lcd.LCD_BACKLIGHT

        # High bits
        Lcd.bus.write_byte(Lcd.I2C_ADDR, bits_high)
        self.lcd_toggle_enable(bits_high)

        # Low bits
        Lcd.bus.write_byte(Lcd.I2C_ADDR, bits_low)
        self.lcd_toggle_enable(bits_low)


    def lcd_toggle_enable(self, bits):
        # Toggle enable
        time.sleep(Lcd.E_DELAY)
        Lcd.bus.write_byte(Lcd.I2C_ADDR, (bits | Lcd.ENABLE))
        time.sleep(Lcd.E_PULSE)
        Lcd.bus.write_byte(Lcd.I2C_ADDR, (bits & ~Lcd.ENABLE))
        time.sleep(Lcd.E_DELAY)


    def lcd_string(self, message, line, align = "left"):
        """
        Displays a message on a specified line of the LCD screen with the given alignment.

        Parameters
        ----------
        message : str
            The text to be displayed on the LCD screen.
        line : int
            The LCD line number (1 to 4) on which to display the message.
        align : str, optional
            The text alignment mode. Options are:
            - "left" (default): Aligns text to the left.
            - "right": Aligns text to the right.
            - "center": Centers the text.

        Notes
        -----
        - If an invalid line number is provided, it defaults to line 1.
        - If an invalid alignment is provided, it defaults to left alignment.
        - The message is longer than LCD width, only the first 16 character will be printed
        """
       
        # Send string to display
        match line:
            case 1:
                line = Lcd.LCD_LINE_1               
            case 2:
                line = Lcd.LCD_LINE_2              
            case 3:
                line = Lcd.LCD_LINE_3               
            case 4:
                line = Lcd.LCD_LINE_4
            case _:
                line = Lcd.LCD_LINE_1

        match align:
            case "left":                           
                message = message.ljust(Lcd.LCD_WIDTH, " ")
            case "right":
                message = message.rjust(Lcd.LCD_WIDTH, " ")
            case "center":               
                message = message.ljust((Lcd.LCD_WIDTH + len(message)) // 2, " ")
                message = message.rjust(Lcd.LCD_WIDTH, " ")
            case _:
                message = message.ljust(Lcd.LCD_WIDTH, " ")

        self.lcd_byte(line, Lcd.LCD_CMD)

        for i in range(Lcd.LCD_WIDTH):
            self.lcd_byte(ord(message[i]), Lcd.LCD_CHR)

if __name__ == '__main__':
    lcd = Lcd()

    lcd.lcd_string("Hello      ", 1)
    lcd.lcd_string("      World", 2)

    time.sleep(3)