#!/bin/python3

from RPi import GPIO
from esc import *

e = ESC()
e.width=2
print(e.freq, e.duty, e.width)
print('Ready to calibrate.  Plug in ESC')
input('Enter after two short beeps')

e.width=1

print(e.freq, e.duty, e.width)

print("If you heard two short beeps, that worked.") 

