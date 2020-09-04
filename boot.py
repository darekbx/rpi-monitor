#
# Startup file for Wio Terminal
#
try:
    from machine import Pin, Map, LCD
except ModuleNotFoundError:
    print("Using virtual machine")
    from virtual_machine import Pin, Map, LCD

import time

led = Pin(Map.LED_BUILTIN, Pin.OUT)

lcd = LCD()
lcd.fillScreen(lcd.color.BLACK)
lcd.setTextColor(lcd.color.WHITE, lcd.color.BLACK)
lcd.drawString("RPI Monitor", 10, 10)

while True:
    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
