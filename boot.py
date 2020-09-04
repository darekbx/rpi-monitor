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

r = 0

while True:

    lcd.setRotation(r)
    lcd.drawString("RPI Monitor", 50, 50)
    r = r + 1

    led.on()
    time.sleep(0.3)
    led.off()
    time.sleep(0.3)
