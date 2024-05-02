import RPi.GPIO as GPIO
import time

# 定義GPIO接腳編號
relay_pin = 17

# 初始化GPIO設置
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# 定義開關函數
# def switch_relay(on):
#     if on:
#         GPIO.output(relay_pin, GPIO.HIGH)
#     else:
#         GPIO.output(relay_pin, GPIO.LOW)

# 讓使用者手動輸入布林值
user_input = input("請輸入 True 或 False：")
input_bool = bool(user_input)

# 控制開關
print (input_bool)

time.sleep(1)
if input_bool == True:
    switch_relay(input_bool)
    time.sleep(3)
    switch_relay(False)
    print('high')
else:
    print('low')
    
    
def switch_relay(input_bool):
    if input_bool == True:
        GPIO.output(relay_pin, GPIO.HIGH)
    else:
        GPIO.output(relay_pin, GPIO.LOW)
print ('ok')
# 釋放GPIO資源
GPIO.cleanup()