import RPi.GPIO as GPIO
import time

# 定義GPIO接腳編號
relay_pin = 17

# 初始化GPIO設置
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# 定義開關函數
def switch_relay(on):
    if on:
        GPIO.output(relay_pin, GPIO.HIGH)
        print('on')
        time.sleep(2)
    else:
        GPIO.output(relay_pin, GPIO.LOW)
        print('off')
        time.sleep(2)
#while True:
switch_relay(True)
#time.sleep(2)
switch_relay(False)
print('ok')

# 釋放GPIO資源
GPIO.cleanup()
print('ook')
