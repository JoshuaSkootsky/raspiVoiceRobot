#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep
#mode = GPIO.getmode()

#print(mode)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

#GPIO.output(4, 0)
#GPIO.output(17, 0)

p1 = GPIO.PWM(4, 1)
p2 = GPIO.PWM(17, 1)

p1.start(50)
sleep(1)
p1.stop()

GPIO.cleanup()
