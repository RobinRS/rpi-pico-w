# Ein einfaches Blink - Programm
import time
from machine import Pin

interne_led = Pin("LED", Pin.OUT)

interne_led.on()
time.sleep_ms(600)  # 600 ms
interne_led.off()
