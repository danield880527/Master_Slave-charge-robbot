import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins_1 = 12
GPIO.setup(pins_1, GPIO.OUT)

pwm = GPIO.PWM(pins_1, 1)
pwm.start(10)
time.sleep(5)
pwm.ChangeFrequency(2)
pwm.ChangeDutyCycle(50)
time.sleep(5)
pwm.stop()
print('ok')
GPIO.cleanup()
