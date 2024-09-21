import json
from array import *
from RPi import GPIO

"""This will initialise an array of pins by setting them as outputs, and turning them off"""


def initialise_outputs(environ, response, parameter = None):
    
    status = "200 OK"
    
    header = [
        ("Content-Type", "application/json"),
        ("Cache-Control", "no-store, no-cache, must-revalidate"),
        ("Expires", "0")
    ]
    
    try:
    
        # pins = array(parameter[0])

        pins = [11, 13, 15, 16, 12, 18, 22, 7, 29, 31]

        # set up all pins to be outputs
        GPIO.setup(pins, GPIO.OUT)

        # turn all pins off
        GPIO.output(pins, 0)

        GPIO.cleanup()
        result = True
    
    except Exception as e:

        status = "400 Bad Request"

        result = str(e)

    response(status, header)

    return [json.dumps(result).encode()]
