#!/usr/bin/python

import os
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

THRESHOLD_ON = 52
THRESHOLD_OFF = 45
INTERVAL = 10 #seconds

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

if __name__ == '__main__':
    try:
        running = False

        while True:
            temp_float = float(getCPUtemperature())
            print("fan_control.py cpu temp: " + str(temp_float))

            if (temp_float > THRESHOLD_ON):
                #turn on fan
                if running == False:
                    print("power on fan...")
                    GPIO.output(14, True)            
                    running = True
            else:
                if running == True and temp_float <= THRESHOLD_OFF:                    
                    #turn off fan
                    print("power off fan...")
                    GPIO.output(14, False)
                    running = False

            time.sleep(INTERVAL)

    except:    
        print("fan_control.py exception caught. power off fan...")
        GPIO.output(14, False)
