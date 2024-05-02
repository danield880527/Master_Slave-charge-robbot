import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
LED_PIN=8
GPIO.setup(LED_PIN,GPIO.OUT)
try:
    while True:
        """GPIO.output(LED_PIN,GPIO.LOW)
        time.sleep(1)"""
        GPIO.output(LED_PIN,GPIO.HIGH)
        time.sleep(1)
        print(LED_PIN)
finally:
    GPIO.cleanup()
