try:
    from machine import Pin, Map
except ModuleNotFoundError:
    print("Using virtual machine")
    from virtual_machine import Pin, Map

class BlueLed:

	_ledPin = None

	def __init__(self):
		self._ledPin = Pin(Map.LED_BUILTIN, Pin.OUT)

	def on(self):
		self._ledPin.on()

	def off(self):
		self._ledPin.off()