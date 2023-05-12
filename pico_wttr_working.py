import time
import network
import urequests as requests
import socket
import json
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
import gc

# set up the hardware, pen p4 to save RAM
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

# set the display backlight to 50%
display.set_backlight(0.5)

# set up constants for drawing
WIDTH, HEIGHT = display.get_bounds()

# set up pens
BLACK = display.create_pen(0, 0, 0)
WHITE = display.create_pen(255, 255, 255)

ssid = 'VM6524115'
password = 'hc2Mpttfq4vh'

gc.enable()

def loop():
    
    response = requests.get(url='http://wttr.in/?format=j2')
    responseText = response.text
    jsonText = json.loads(response.text)
    conditionsDict = jsonText["current_condition"][0]
    areaDict = jsonText["nearest_area"][0]
    location = (areaDict["areaName"][0]["value"])
    region = (areaDict["region"][0]["value"])
    country = (areaDict["country"][0]["value"])
    locationString = (location + ", " + region + ", " + country)

    tempC = conditionsDict["temp_C"]
    feelsLikeC = conditionsDict["FeelsLikeC"]
    windSpeedKmph = conditionsDict["windspeedKmph"]
    windDir = conditionsDict['winddir16Point']
    desc = (conditionsDict["weatherDesc"][0])["value"]

    display.set_pen(BLACK)
    display.clear()
    display.set_pen(WHITE)
    display.set_font("bitmap8")
    display.text(locationString, 0, 0, scale = 1)
    display.text(desc, 0, 20, scale=2)
    display.text("Temperature: " + tempC + "\xb0c", 0, 38, scale=2)
    display.text("Feels Like: " + feelsLikeC + "\xb0c", 0, 56, scale = 2)
    display.text("Wind Speed: " + windSpeedKmph + "km/h", 0, 74, scale = 2)
    display.text("Wind Dir: " + windDir, 0, 92, scale = 2)
    display.update()

    response.close()

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
 
# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)
 
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    while True:
        loop()
        gc.collect()
        time.sleep(1800)
