from machine import Pin
import neopixel
import utime
from math import fmod
from extra_math import Map

PIXEL_NUMBER = 90

pixels = neopixel.NeoPixel(Pin(0, Pin.OUT), PIXEL_NUMBER)
brightness = 255

def getRGB (numbercode):
  r = 0
  g = 0
  b = 0
  self_numbercode = fmod(numbercode, 764)
  if self_numbercode <= 255:
    r = 255 - self_numbercode
    g = self_numbercode
    b = 0
  if self_numbercode > 255 and self_numbercode <= 510:
    r = 0
    g = 510 - self_numbercode
    b = self_numbercode - 255
  if self_numbercode > 510 and self_numbercode < 765:
    r = self_numbercode - 510
    g = 0
    b = 765 - self_numbercode
  
  r = Map(r, 0, 255, 0, brightness)
  g = Map(g, 0, 255, 0, brightness)
  b = Map(b, 0, 255, 0, brightness)
  
  return [int(r), int(g), int(b)]

i = 0

dim = 0 # the higher the value, the more "washed-out" the colors are

colorDeviation = 10 # a value of 76 makes a rainbow
delay = 0

while True:
  for i in range(0, 765, 5):
    for j in range(PIXEL_NUMBER):
      code = i + (j * colorDeviation)

      red = getRGB(code)[0]
      green = getRGB(code)[1]
      blue = getRGB(code)[2]

      if j < 4:
        red = red - ((4 - j) * dim)
        green = green - ((4 - j) * dim)
        blue = blue - ((4 - j) * dim)
      if j > 4:
        red = red - ((j - 4) * dim)
        green = green - ((j - 4) * dim)
        blue = blue - ((j - 4) * dim)

      if red < 0:
        red = 0
      if green < 0:
        green = 0
      if blue < 0:
        blue = 0

      rgb = [red, green, blue]
      
      pixels[j] = (rgb[0], rgb[1], rgb[2])
    utime.sleep_ms(delay)
    pixels.write()