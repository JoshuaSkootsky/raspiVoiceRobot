#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

#mode = GPIO.getmode()

#print(mode)
GPIO.setmode(GPIO.BCM)

def robot_GO():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    GPIO.output(4, 1)
    GPIO.output(17, 1)

    sleep(5)

    GPIO.output(4, 0)
    GPIO.output(17, 0)

    sleep(5)

    GPIO.output(17, 1)

    sleep(5)

    GPIO.output(17, 0)

    sleep(5)

    GPIO.output(4, 1)

    sleep(5)

    GPIO.output(4, 0)

    sleep(5)

    GPIO.output(4, 1)
    GPIO.output(17, 1)

    sleep(7)

    GPIO.cleanup()



