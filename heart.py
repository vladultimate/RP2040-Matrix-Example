from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms

pixels = NeoPixel(Pin(16), 25)

heart_pixel = [1,3,5,9,6,7,8,10,14,11,12,13,16,17,18,22]

def heart():
    for pixel in heart_pixel:
        pixels[pixel] = (0,5,0)  
        pixels.write()
        sleep_ms(30)

    sleep_ms(200)

    for pixel in heart_pixel[::-1]:
        pixels[pixel] = (0,0,0)
        pixels.write()
        sleep_ms(75)
    
while True:
    heart()
    sleep_ms(100)
