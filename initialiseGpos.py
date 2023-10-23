#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import logging
from datetime import datetime


now = datetime.now() # current date and time
logfilename = datetime.now().strftime("%Y%m%d") + "-initialiseGpios.log"

logging.basicConfig(filename=logfilename, filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info("Starting new GPIO Initialisation")
#GPIO BCM details:
#lawn   GPIO#s: 0, 1, 2, 3, 4, 5
#garden GPIO#s: 6, 7, 21, 22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#define the pins
pins = [11, 12, 13, 15, 16, 18,
        22, 7, 29, 31]

#https://sourceforge.net/p/raspberry-gpio-python/wiki/Outputs/

#turn all pins off
#GPIO.setup(pins, GPIO.OUT)
#GPIO.output(pins, 0)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)
    logging.info("Pin " + str(pin) + " current value: " + str(GPIO.input(pin)))
    GPIO.output(pin, 0)
    logging.info("Pin " + str(pin) + " should now be off: " + str(GPIO.input(pin)))
    #GPIO.output(pin, 1)
    #logging.info("Pin " + str(pin) + " should should be on: " + str(GPIO.input(pin)))
    #logging.info("Initialisation completed for pin " + str(pin) + "!\n")

#release the pins
GPIO.cleanup()

logging.info("GPIO Initialisation completed.--------------------------------------------------")