#!/bin/python3

from RPi import GPIO
from esc import *

e = ESC()
e.change_pulse_width(1.5)


