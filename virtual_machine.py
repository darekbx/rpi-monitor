'''
Implementation of basic methods for Seeed Wio Terminal (using ArduPy)
This class is useful when you need to test your code without physical device 

based on: https://wiki.seeedstudio.com/ArduPy-LCD/
'''

import pygame
import threading

class LCD:
	
	class color:
		BLACK = (0, 0, 0)
		BLUE = (0, 0, 255)
		CYAN = (0, 238, 238)
		DARKCYAN = (0, 139, 139)
		DARKGREEN = (0, 100, 0)
		DARKGREY = (100, 100, 100)
		GREEN = (0, 200, 0)
		GREENYELLOW = (173, 255, 47)
		LIGHTGREY = (211, 211, 211)
		MAGENTA = (255, 0, 255)
		MAROON = (255, 52, 179)
		NAVY = (0, 0, 128)
		OLIVE = (107, 142, 35)
		ORANGE = (255, 165, 0)
		PINK = (255, 192, 203)
		PURPLE = (102, 0, 102)
		YELLOW = (238, 238, 0)
		WHITE = (255, 255, 255)
		RED = (255, 0, 0)
		
	FPS = 3

	width = 320
	height = 240

	_screen = None
	_clock = None

	_rotation = None
	_screenColor = (0, 0, 0)

	_textColor = color.WHITE
	_textBgColor = color.BLACK
	_fontSize = 12
	_font = None

	def __init__(self):
		super().__init__()

		pygame.init()

		self._font = pygame.font.Font(pygame.font.get_default_font(), self._fontSize)
		self._screen = pygame.display.set_mode((self.width, self.height))
		self._screen.fill(self._screenColor)
		self._clock = pygame.time.Clock()

		threading.Thread(target=self._refreshThread).start()

	def _refreshThread(self):
		done = False
		while not done:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					done = True
			self._draw()
			pygame.display.update()
			self._clock.tick(self.FPS)

	def _draw(self):

		#self._screen.fill(self._screenColor)
		
		self._applyRotation()

	def color16to8(self, color):
		raise Exception("Not implemented")

	def getCursorX(self):
		raise Exception("Not implemented")

	def getCursorY(self):
		raise Exception("Not implemented")

	def getRotation(self):
		raise Exception("Not implemented")

	def getTextDatum(self):
		raise Exception("Not implemented")

	def setRotation(self, r):
		"""Set virtual display rotation

        Parameters
        ----------
        r : int
            Rotation (0: rotate 0 degrees, 1: rotate 90 degrees, 2: rotate 180 degrees, 3: rotate 270 degrees)
        """
		self._rotation = r

	def setTextColor(self, color):
		self._textColor = color

	def setTextColor(self, fgColor, bgColor):
		self._textColor = fgColor
		self._textBgColor = bgColor

	def drawCentreString(self, string, dX, poY, font = None):
		raise Exception("Not implemented")

	def drawString(self, string, poX, poY, font = None): 
		text_surface = self._font.render(string, True, self._textColor)
		text_width, text_height = self._font.size(string)
		pygame.draw.rect(self._screen, self._textBgColor, [poX, poY, text_width, text_height]) 
		self._screen.blit(text_surface, dest=(poX,poY))

	def drawChar(self, char, poX, poY):
		raise Exception("Not implemented")

	def drawCircle(self, x0, y0, r, color):
		raise Exception("Not implemented")

	def drawCircleHelper(self, x0, y0, r, cornername, color):
		raise Exception("Not implemented")

	def drawEllipse(self, x, y, rx, ry, color):
		raise Exception("Not implemented")

	def drawFastHLine(self, x, y, w, color):
		raise Exception("Not implemented")

	def drawFastVLine(self, x, y, h, color):
		raise Exception("Not implemented")

	def drawFloat(self, floatNumber, decimal, x, y , font):
		raise Exception("Not implemented")

	def drawLine(self, x, y, x1, y1, color):
		pygame.draw.line(self._screen, color, (x, y), (x1, y1))

	def drawNumber(self, number, x, y, font):
		raise Exception("Not implemented")

	def drawPixel(self, x, y, color):
		raise Exception("Not implemented")

	def drawRect(self, x, y, w, h, color):
		raise Exception("Not implemented")

	def drawRoundRect(self, x, y, w, h, r, color):
		raise Exception("Not implemented")

	def drawTriangle(self, x0, y0, x1, y1, x2, y2, color):
		raise Exception("Not implemented")

	def fillCircle(self, x0, y0, r, color):
		raise Exception("Not implemented")

	def fillCircleHelper(self, x0, y0, r, cornername, color):
		raise Exception("Not implemented")

	def fillEllipse(self, x, y, rx, ry, color):
		raise Exception("Not implemented")

	def fillRect(self, x, y, w, h, color):
		pygame.draw.rect(self._screen, color, [x, y, w, h])

	def fillRoundRect(self, x, y, w, h, r, color):
		raise Exception("Not implemented")

	def fillTriangle(self, x0, y0, x1, y1, x2, y2, color):
		raise Exception("Not implemented")

	def fillScreen(self, color):
		self._screenColor = color

	def invertDisplay(self, n):
		raise Exception("Not implemented")

	def setPivot(self, x, y):
		raise Exception("Not implemented")

	def setTextDatum(self, datum):
		raise Exception("Not implemented")

	def setTextFont(self, font):
		raise Exception("Not implemented")

	def setTextSize(self, size):
		self._fontSize = size
		self._font = pygame.font.Font(pygame.font.get_default_font(), self._fontSize)

	def textWidth(self, string):
		raise Exception("Not implemented")

	def _applyRotation(self):
		if self._rotation is not None:
			angle = 0
			normalizedRotation = self._rotation - (self._rotation // 4) * 4

			if normalizedRotation == 0:
				angle = 0
			elif normalizedRotation == 1:
				angle = 90
			elif normalizedRotation == 2:
				angle = 180
			elif normalizedRotation == 3:
				angle = 270
			
			self._screen.blit(pygame.transform.rotate(self._screen, angle), (0, 0))

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
		raise Exception("Not implemented")
	
	def off(self):
		raise Exception("Not implemented")

class Map:

	LED_BUILTIN = 50
	WIO_KEY_A = 55
	WIO_KEY_B = 56
	WIO_KEY_C = 57
	WIO_5S_LEFT = 59
	WIO_5S_RIGHT = 60
	WIO_5S_UP = 58
	WIO_5S_DOWN = 61
	WIO_5S_PRESS = 62