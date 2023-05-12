import time
import network
import urequests as requests
import json
import gc
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

# set up the hardware, pen p4 to save RAM
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

# set the display backlight to 50%
display.set_backlight(0.5)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()

# set up pens
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)

# add wifi connection info
ssid = ''
password = ''

# enable garbage collection
gc.enable()
# main loop
def loop():
    
    # send get request to 'http://wttr.in/?format=j2'
    
    
    # extract and manipulate json


    # draw to the display


    # close connection


# connect to wlan
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
 
# wait for connection

 
# handle connection error before running main loop
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    while True:
        loop()
        gc.collect()
        time.sleep(1800)

