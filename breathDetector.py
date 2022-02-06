from adafruit_circuitplayground import cp
import math
import time
import array
import audiobusio
import board
while True:
    if cp.button_a: # longer breaths = longer pinwheel time
        mic = audiobusio.PDMIn(
            board.MICROPHONE_CLOCK,
            board.MICROPHONE_DATA,
            sample_rate=16000,
            bit_depth=16
        )
        def mean(values):
            return sum(values) / len(values)
        def normalized_rms(values):
            minbuf = int(mean(values))
            sum_of_samples = sum(
                float(sample - minbuf) * (sample - minbuf)
                for sample in values
            )
            return math.sqrt(sum_of_samples / len(values))
        def sound_level():
            samples = array.array('H', [0] * 160)
            mic.record(samples, len(samples))
            magnitude = normalized_rms(samples)
            return magnitude
        while True:
            if math.log(sound_level()) > 7:
                for loop_number in range(0, 10, 1):
                    cp.pixels[loop_number] = (255, 0, 0)
                    time.sleep(0.1)
                    cp.pixels[loop_number] = (0, 0, 0)
            time.sleep(.001)
        light_show(encoding)

# Write your code here :-)
