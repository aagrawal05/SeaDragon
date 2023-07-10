import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# R
GPIO.setup(22, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
PWMR = GPIO.PWM(10, 100)

GPIO.output(22, GPIO.HIGH)
PWMR.start(5)
time.sleep(1)
GPIO.output(22, GPIO.LOW)
PWMR.start(5)
time.sleep(1)

GPIO.cleanup()
