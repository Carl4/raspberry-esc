#!/bin/python3

from RPi import GPIO

class ESC(object):

    def __init__(self, mode=GPIO.BCM, pin_number=18, freq=100, duty=0): 

        GPIO.setmode(mode)
        self.mode=mode
        self.pin_number=pin_number
        self._freq=freq
        self._duty=duty
        GPIO.setup(pin_number, GPIO.OUT)
        self._p = GPIO.PWM(pin_number, freq)
        self._p.start(0)

    @property 
    def freq(self):
        return self._freq

    @freq.setter
    def freq(self, freq):
        self._freq=freq
        self._p.ChangeFrequency(freq)


    @property
    def duty(self):
        return self._duty

    @duty.setter
    def duty(self, duty):
        self._duty=duty
        self._p.ChangeDutyCycle(duty)

    # w = 10* d/f d = w*f / 10
    @property
    def width(self):
        "Returns the pulse width in ms"
        return self._duty / self._freq * 10

    @width.setter 
    def width(self, width):
        "Sets the pulse width in ms"
        # Remember that duty cycle is in %, so 
        # 100*width(ms)/1000 * freq
        self.duty = width/10 * self._freq



