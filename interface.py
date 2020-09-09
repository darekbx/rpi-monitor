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
from key_map import KeyMap

IS_VIRTUAL_MACHINE = False

try:
    from machine import LCD, Pin
except ModuleNotFoundError:
	print("Using virtual machine")
	IS_VIRTUAL_MACHINE = True
	from virtual_machine import LCD, Pin

class MainMenu:

	MAIN_LOOP_DELAY = 0.1

	def draw(self):
		lcd = LCD()
		lcd.fillScreen(LCD.color.BLACK)
		lcd.setTextColor(LCD.color.WHITE, LCD.color.DARKGREY)

		if IS_VIRTUAL_MACHINE:
			lcd.keyCallback = self.keyCallback

		while True:
			self.drawMenuButton(lcd, KeyMap.WIO_KEY_A, "MENU", 0)
			self.drawMenuButton(lcd, KeyMap.WIO_KEY_B, "LOCK", 1)
			self.drawMenuButton(lcd, KeyMap.WIO_KEY_C, "WIFI", 2)

			lcd.setTextColor(LCD.color.WHITE, LCD.color.BLACK)
			lcd.drawCentreString("Terminal", 150, 110)

			lcd.drawLine(int(60), int(0), int(60), int(20), LCD.color.WHITE)
			lcd.drawLine(int(120), int(0), int(120), int(20), LCD.color.WHITE)
			lcd.drawLine(int(180), int(0), int(180), int(20), LCD.color.WHITE)
			lcd.drawLine(int(0), int(20), int(180), int(20), LCD.color.WHITE)

			time.sleep(self.MAIN_LOOP_DELAY)

	def drawMenuButton(self, lcd, button, title, index):
		pin = Pin(button, Pin.IN, Pin.PULL_UP)
		if IS_VIRTUAL_MACHINE:
			self.setValue(pin, button)
		if pin.value() == KeyMap.HIGH:
			lcd.setTextColor(LCD.color.WHITE, LCD.color.RED)
			lcd.fillRect(index * 60, 0, 60, 20, LCD.color.RED)
		else:
			lcd.setTextColor(LCD.color.WHITE, LCD.color.DARKGREY)
			lcd.fillRect(index * 60, 0, 60, 20, LCD.color.DARKGREY)
		lcd.drawString(title, index * 60 + 5, 5)

	# Baypass pygame keyboar input to pin
	# Method only for virtual machine
	_state_map = { }
	def keyCallback(self, key):
		if key == 'A':
			self._state_map[KeyMap.WIO_KEY_A] = KeyMap.HIGH 
		elif key == 'B':
			self._state_map[KeyMap.WIO_KEY_B] = KeyMap.HIGH
		elif key == 'C':
			self._state_map[KeyMap.WIO_KEY_C] = KeyMap.HIGH

	def setValue(self, pin, key):
		if key in self._state_map:
			pin.setValue(self._state_map[key])
			del self._state_map[key]
	
	def dump(self, lcd):
		x = 5
		y = 25
		for c in dir(Pin):
			value = getattr(Pin, c)
			lcd.drawString("{0}: {1}".format(c, value), x, y)
			y += 15
			if y > 200:
				y = 25
				x += 100




