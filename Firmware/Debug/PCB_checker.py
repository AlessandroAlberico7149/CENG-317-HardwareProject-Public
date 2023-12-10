#Testing transistor and LED (to make sure everything is connected)

import RPi.GPIO as GPIO
import time

#LED pin, connected to 220Ω via positive 3V3 pin 17
LED_PIN = 17

#Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#Turn on the LED
def turn_on_led():
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED ON")

#Turn off the LED
def turn_off_led():
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED OFF")
    
# Main
try:
    while True:
        #Turn on the LED
        turn_on_led()
        time.sleep(3)

        #Turn off the LED
        turn_off_led()
        time.sleep(3)

finally:
    #Clean up GPIO on program exit
    GPIO.cleanup()
