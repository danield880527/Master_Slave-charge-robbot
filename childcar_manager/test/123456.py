import RPi.GPIO as GPIO
import time

# 定義GPIO接腳編號
relay_pin = 17

# 初始化GPIO設置
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

while True:
    GPIO.output(relay_pin,GPIO.HIGH)
    print('relay on')
    time.sleep(2)
    GPIO.output(relay_pin,GPIO.LOW)
    print('relay off')
    time.sleep(2)