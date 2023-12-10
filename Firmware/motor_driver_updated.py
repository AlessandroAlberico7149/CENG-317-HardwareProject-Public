#name: Alessandro Alberico
#Student Number: n01417149
#reference: https://qwiic-scmd-py.readthedocs.io/en/latest/ex2.html
#NOTE: SETTING THE SPEED TO LESS THAN 200 WILL MAKE THE MOTOR RUN BUT IT WON'T TURN

from __future__ import print_function
import time
import sys
import math
import qwiic_scmd

myMotor = qwiic_scmd.QwiicScmd()

#Coils variables (the motor numbers, whereas Motor A is coil A and motor B is coil B)
COIL_A = 0
COIL_B = 1
#Clockwise
CW = 0
#Counter-clockwise
CCW = 1

#Sequence clockwise
coil_sequence_unipolar = [
    [1, 0, 0, 0],  #Coil 1
    [0, 1, 0, 0],  #Coil 2
    [0, 0, 1, 0],  #Coil 3
    [0, 0, 0, 1],  #Coil 4
]

coil_sequence_bipolar = [
    [0, 0, 0, 1],  #Coil 4
    [0, 0, 1, 0],  #Coil 3
    [0, 1, 0, 0],  #Coil 2
    [1, 0, 0, 0],  #Coil 1
]

#motors
bipolar = 1
unipolar = 0


def runStepper(direction, speed, steps, motor_type):

    if myMotor.connected == False:
        print("Motor Driver not connected. Check connections and try again.", file=sys.stderr,)
        return
    else:
        print("Motor recognized\nConnected to I2C address 0x{:02X}".format(myMotor.address))

    if motor_type == unipolar:
        coil_sequence_used = coil_sequence_unipolar
    else:
        coil_sequence_used = coil_sequence_bipolar

    myMotor.begin()
    print("initializing Motor")
    time.sleep(0.250)

    # Zero Motor Speed
    myMotor.set_drive(0, 0, 0)
    myMotor.set_drive(1, 0, 0)

    myMotor.enable()
    print("Motor enabled")
    time.sleep(0.250)

    print(
        "Stepper Motor running at\n{} velocity, direction {} with {} steps.".format(
            speed, "Clockwise" if direction == CW else "Counter-clockwise", steps))
    count = 0

    if (direction == CCW and motor_type == bipolar) or (direction == CW and motor_type == unipolar):
        for step in range(steps):
            for coil in coil_sequence_used:
                myMotor.set_drive(COIL_A, coil[0], speed)
                myMotor.set_drive(COIL_B, coil[1], speed)
                myMotor.set_drive(COIL_A, coil[2], speed)
                myMotor.set_drive(COIL_B, coil[3], speed)
                time.sleep(0.009)
                if count == 20:
                    print("Step {}/{} completed".format(step, steps))
                    count = 0
                count += 1
    else:
        for step in range(steps):
            for coil in coil_sequence_used:
                myMotor.set_drive(COIL_B, coil[0], speed)
                myMotor.set_drive(COIL_A, coil[1], speed)
                myMotor.set_drive(COIL_B, coil[2], speed)
                myMotor.set_drive(COIL_A, coil[3], speed)
                time.sleep(0.009)
                if count == 20:
                    print("Step {}/{} completed".format(step, steps))
                    count = 0
                count += 1

    #Disable motor after completing steps
    myMotor.disable()
    print("Motor disabled")


# main
if __name__ == "__main__":
    try:
        #stepper motor in the clockwise direction, speed 100, for 200 steps
        runStepper(CW, 300, 100, bipolar)
                       
        #stepper motor in the counter-clockwise direction, speed 100, for 200 steps
        runStepper(CCW, 300, 100, bipolar)

    except (KeyboardInterrupt, SystemExit) as exErr:
        print("Ending motor driver")
        myMotor.disable()
        sys.exit(0)
