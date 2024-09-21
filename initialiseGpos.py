#!/usr/bin/python3

import RPi.GPIO as GPIO
import time
import logging
from datetime import datetime


now = datetime.now() # current date and time
logfilename = datetime.now().strftime("%Y%m%d") + "-initialiseGpios.log"

logging.basicConfig(filename=logfilename, filemode='w',format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info("Starting new GPIO Initialisation")
logging.info("Note that this is just an explicit operation normally performed by the pinitialise.service")
logging.info("for more information, refer to the pinitialise github repo: https://github.com/johnnyreid/pinitialise")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# This is a Raspberry Pi 1 Model B+
# Relay | GPIO# | PIN | Broadcom number (used by pigpio)
# 1     | 0     | 11  | 17
# 2     | 1     | 13  | 27
# 3     | 2     | 15  | 22
# 4     | 3     | 16  | 23
# 5     | 4     | 12  | 18
# 6     | 5     | 18  | 24
# 7     | 6     | 22  | 25
# 8     | 7     | 7   | 4
# 9     | 21    | 29  | 5
# 10    | 22    | 31  | 6

# Not in use:
# 11    | 23    | 33  | 13
# 12    | 24    | 35  | 19
# 13    | 25    | 37  | 26
# 14    | 26    | 32  | 12
# 15    | 27    | 36  | 16
# 16    | 28    | 38  | 20

# GPIO BCM details:
# lawn   GPIO#s: 0, 1, 2, 3, 4, 5
# garden GPIO#s: 6, 7, 21, 22

#define the pins using their pin number, not their broadcom number
pins = [11, 13, 15, 16, 12, 18,
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