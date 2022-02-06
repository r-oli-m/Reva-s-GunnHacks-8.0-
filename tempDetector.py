from adafruit_circuitplayground import cp
import math
import time
import array
import audiobusio
import board

while True:
    if cp.button_b: #temperature+sound
        print('hello')
        cp.pixels.auto_write = False
        cp.pixels.brightness = 0.25
        # in Celcius
        minimum_temp = 26
        maximum_temp = 30
        def scale_range(value):
            return int((value - minimum_temp) / (maximum_temp - minimum_temp) * 10)
        while True:
            peak = scale_range(cp.temperature)
            print(cp.temperature)
            print(int(peak))
            for i in range(10):
                if i <= peak:
                    cp.pixels[i] = (0, 255, 255)
                else:
                    cp.pixels[i] = (0, 0, 0)
            cp.pixels.show()
            time.sleep(0.05)
