from __future__ import print_function
from pidigits import piGenLeibniz as piGenerator
from time import sleep
import sys

interval = 0.3
multiplier = 0.992

mypi = piGenerator()
print(str(next(mypi)) + ".", end="")
sys.stdout.flush()
sleep(interval)

while(True):
    interval = interval * multiplier
    print(next(mypi), end="")
    sys.stdout.flush()
    sleep(interval)
