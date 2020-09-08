'''
 - Show lock Screen (with PIN) after start, after unlock main screen is shown
 - Main screen
   - Top menu: Menu, Lock, Wifi Status
   - Menu options:
     - Scanning Device tester
	 - BT Scanner/Sniffer
	 - Wifi options
	 - File manager
	 - RSS reader

'''
import time

try:
    from machine import LCD, Map, Pin
except ModuleNotFoundError:
    print("Using virtual machine")
    from virtual_machine import LCD, Map, Pin

class MainMenu:

	def draw(self):
		lcd = LCD()
		lcd.fillScreen(LCD.color.BLACK)
		lcd.setTextColor(LCD.color.WHITE, LCD.color.DARKGREY)

		lcd.fillRect(0, 0, 180, 20, LCD.color.DARKGREY)
		lcd.drawLine(int(60), int(0), int(60), int(20), LCD.color.WHITE)
		lcd.drawLine(int(120), int(0), int(120), int(20), LCD.color.WHITE)
		lcd.drawLine(int(180), int(0), int(180), int(20), LCD.color.WHITE)
		lcd.drawLine(int(0), int(20), int(180), int(20), LCD.color.WHITE)

		#button = Pin(Map.WIO_KEY_B, Pin.IN, Pin.PULL_UP)

		lcd.drawString("MENU", 5, 5)
		lcd.drawString("LOCK", 65, 5)
		lcd.drawString("WIFI", 125, 5)

		self.dump(lcd)

	def dump(self, lcd):
		x = 5
		y = 25
		for c in dir(Map):
			value = getattr(Map, c)
			lcd.drawString("{0}: {1}".format(c, value), x, y)
			y += 15
			if y > 200:
				y = 25
				x += 100




