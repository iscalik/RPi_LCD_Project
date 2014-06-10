#
#Raspberry Pi LCD Project
#Ismet Said Calik
#http://ismetsaidcalik.com
#
# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)          - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0                   - NOT USED
# 8 : Data Bit 1                   - NOT USED
# 9 : Data Bit 2                   - NOT USED
# 10: Data Bit 3                   - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND


def lcd_yaz():
	from datetime import datetime # imported library
	from time import sleep
	from LCDLib import *
	lcd_init()
	try:
    		while True:
        		lcd_byte(LCD_LINE_1, LCD_CMD)
	        	lcd_string(datetime.now().strftime('%H:%M:%S')) #(firtst row)Write to LCD time
        		lcd_byte(LCD_LINE_2, LCD_CMD)
        		lcd_string(datetime.now().strftime('%a %d %b %y'))#(second row) Write to LCD date
        		sleep(1)
	except KeyboardInterrupt:
    		lcd_clear()
