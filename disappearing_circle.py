from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

pixels = NeoPixel(Pin(16), 25)

big_bouble = [1,2,3,5,9,10,14,15,19,21,22,23]

def circle():
    for pixel in big_bouble:
        pixels[pixel] = (5,5,20)  
        pixels.write()
        sleep_ms(75)

    sleep_ms(75)

    for pixel in big_bouble[::-1]:
        pixels[pixel] = (0,0,0)
        pixels.write()
        sleep_ms(75)

while True:
    circle()
    sleep_ms(100)
