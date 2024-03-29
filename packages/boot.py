# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

from machine import SoftI2C, Pin
from lis2hh12 import LIS2HH12, SF_G
from neopixel import NeoPixel

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
imu = LIS2HH12(i2c, address=0x18, sf=SF_G)
# enable the ACC interrupt to turn on backlight
imu.enable_act_int()

neopixel_pin = Pin(2, Pin.OUT)
neopixels = NeoPixel(neopixel_pin, 5)
neopixels[0] = (0,0,0)
neopixels[1] = (0,0,0)
neopixels[2] = (0,0,0)
neopixels[3] = (0,0,0)
neopixels[4] = (0,0,0)
neopixels.write()

import settings

if settings.get('BLE-beacon_enabled'):
    import BLE_beacon

if settings.get('wifi.enabled'):
    import wifi
    
import apps.menu