import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
    def aan(self):
        GPIO.output(self.pin, GPIO.HIGH)
    def uit(self):
        GPIO.output(self.pin, GPIO.LOW)

led1 = Led(7)
led2 = Led(23)

while True:
    led1.aan()
    led2.aan()
    time.sleep(1)
    led1.uit()
    time.sleep(1)
    led2.uit()
    time.sleep(1)
