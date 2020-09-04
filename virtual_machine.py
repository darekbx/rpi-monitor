'''
Implementation of basic methods for Seeed Wio Terminal (using ArduPy)
This class is useful when you need to test your code without physical device 

based on: https://wiki.seeedstudio.com/ArduPy-LCD/
'''
class LCD:
	
	class color:
		BLACK = (255, 0, 0, 0)
		WHITE = (255, 255, 255, 255)

	width = 320
	height = 240

	def color16to8(self, color):
		pass

	def getCursorX(self):
		pass

	def getCursorY(self):
		pass

	def getRotation(self):
		pass

	def getTextDatum(self):
		pass

	def setRotation(self, r):
		pass

	def setTextColor(self, color):
		pass

	def setTextColor(self, fgColor, bgColor):
		pass

	def drawCentreString(self, string, dX, poY, font):
		pass

	def drawString(self, string, poX, poY, font): 
		pass

	def drawChar(self, char, poX, poY):
		pass

	def drawCircle(self, x0, y0, r, color):
		pass

	def drawCircleHelper(self, x0, y0, r, cornername, color):
		pass

	def drawEllipse(self, x, y, rx, ry, color):
		pass

	def drawFastHLine(self, x, y, w, color):
		pass

	def drawFastVLine(self, x, y, h, color):
		pass

	def drawFloat(self, floatNumber, decimal, x, y , font):
		pass

	def drawLine(self, x, y, x1, x2, color):
		pass

	def drawNumber(self, number, x, y, font):
		pass

	def drawPixel(self, x, y, color):
		pass

	def drawRect(self, x, y, w, h, color):
		pass

	def drawRoundRect(self, x, y, w, h, r, color):
		pass

	def drawTriangle(self, x0, y0, x1, y1, x2, y2, color):
		pass

	def fillCircle(self, x0, y0, r, color):
		pass

	def fillCircleHelper(self, x0, y0, r, cornername, color):
		pass

	def fillEllipse(self, x, y, rx, ry, color):
		pass

	def fillRect(self, x, y, w, h, color):
		pass

	def fillRoundRect(self, x, y, w, h, r, color):
		pass

	def fillTriangle(self, x0, y0, x1, y1, x2, y2, color):
		pass

	def fillScreen(self, color):
		pass

	def invertDisplay(self, n):
		pass

	def setPivot(self, x, y):
		pass

	def setTextDatum(self, datum):
		pass

	def setTextFont(self, font):
		pass

	def setTextSize(self, size):
		pass

	def textWidth(self, string):
		pass

class Pin:

	OUT = "pin_output"
	IN = "pin_input"

	_pin = None
	_mode = None

	def __init__(self, pin, mode):
		super().__init__()
		self._pin = pin
		self._mode = mode
		
	def on(self):
		pass
	
	def off(self):
		pass

class Map:

	LED_BUILTIN = 13