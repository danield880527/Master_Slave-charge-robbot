import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED_PIN=16
GPIO.setup(LED_PIN,GPIO.OUT)
ppwm=GPIO.PWM(LED_PIN,1000)
ppwm.start(0)
duty=100
try:
	while True:
		ppwm.ChangeDutyCycle(duty)
		time.sleep(0.1)
finally:
	GPIO.ckeanup()

