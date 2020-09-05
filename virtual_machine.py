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
		WHITE = (255, 255, 255)

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
		pass

	def drawString(self, string, poX, poY, font = None): 
		text_surface = self._font.render(string, True, self._textColor)
		self._screen.blit(text_surface, dest=(poX,poY))

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

	def drawLine(self, x, y, x1, y1, color):
		pygame.draw.line(self._screen, color, (x, y), (x1, y1))

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
		self._screenColor = color
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
		self._fontSize = size
		self._font = pygame.font.Font(pygame.font.get_default_font(), self._fontSize)

	def textWidth(self, string):
		pass

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
		pass
	
	def off(self):
		pass

class Map:

	LED_BUILTIN = 13