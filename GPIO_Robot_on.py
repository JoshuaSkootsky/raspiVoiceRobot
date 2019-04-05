#!/usr/bin/env python3

import RPi.GPIO as GPIO

#mode = GPIO.getmode()

#print(mode)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

GPIO.output(4, 1)
GPIO.output(17, 1)



