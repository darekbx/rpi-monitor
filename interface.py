import time

try:
    from machine import LCD
except ModuleNotFoundError:
    print("Using virtual machine")
    from virtual_machine import LCD

class MainMenu:

	def draw(self):
		lcd = LCD()
		lcd.fillScreen(LCD.color.BLACK)
		lcd.setTextColor(LCD.color.WHITE, LCD.color.BLACK)
		lcd.drawString("RPI Monitor2", 50, 50)
		lcd.drawLine(int(10), int(10), int(50), int(50), LCD.color.WHITE)