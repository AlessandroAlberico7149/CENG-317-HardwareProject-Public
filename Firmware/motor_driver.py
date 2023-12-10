#name: Alessandro Alberico
#Student Number: n01417149
#reference: https://qwiic-scmd-py.readthedocs.io/en/latest/ex2.html

from __future__ import print_function
import time
import sys
import math
import qwiic_scmd

myMotor = qwiic_scmd.QwiicScmd()

#needed variables
COIL_A = 0
COIL_B = 1
#Clockwise
CW = 0
#Counter-clockwise
CCW = 1

def runStepper(direction, speed, steps):
    print(f"Stepper Motor running at: {speed} velocity, towards {direction} with {steps} steps.")
    
    if myMotor.connected == False:
        print("Motor Driver not connected. Check connections and try again.", file=sys.stderr)
        return

    myMotor.begin()
    print("Motor initialized.")
    time.sleep(.250)
    
    #Zero Motor Speed
    myMotor.set_drive(0, 0, 0)
    myMotor.set_drive(1, 0, 0)
    
    myMotor.enable()
    print("Motor enabled")
    time.sleep(.250)
    
    for _ in range(steps):
        print(speed)
        myMotor.set_drive(COIL_A, direction, speed)
        myMotor.set_drive(COIL_B, direction, speed)
        time.sleep(.05)

    #Disable motor after completing steps
    myMotor.disable()
    print("Motor disabled")
    
    
#main
if __name__ == '__main__':
    try:
        #stepper motor in the clockwise direction, speed 100, for 200 steps
        runStepper(CW, 100, 200)
        #stepper motor in the counter-clockwise direction, speed 100, for 200 steps
        runStepper(CCW, 100, 200)
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending example.")
        myMotor.disable()
        sys.exit(0)