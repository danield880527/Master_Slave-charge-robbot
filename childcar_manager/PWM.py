import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
LED_PIN=16
GPIO.setup(LED_PIN,GPIO.OUT)
ppwm=GPIO.PWM(LED_PIN,1000)
ppwm.start(0)

try:
	while True:
		for duty in range(0,101,1):
			ppwm.ChangeDutyCycle(duty)
			time.sleep(0.1)
			print(duty)
		time.sleep(0.5)
		for duty in range(100,-1,-1):
			ppwm.ChangeDutyCycle(duty)
			time.sleep(0.1)
			print(duty)
		time.sleep(0.5)
finally:
	GPIO.ckeanup()

