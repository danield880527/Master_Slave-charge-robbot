import RPi.GPIO as GPIO
import time

# 定義GPIO接腳編號
relay_pin = 18

# 初始化GPIO設置
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

# 定義開關函數
def switch_relay(on):
    if on:
        GPIO.output(relay_pin, GPIO.HIGH)
    else:
        GPIO.output(relay_pin, GPIO.LOW)

# 讓使用者手動輸入布林值
user_input = input("請輸入 True 或 False：")
input_bool = bool(user_input)

# 控制開關
switch_relay(input_bool)  # 控制電磁鐵

# 釋放GPIO資源
GPIO.cleanup()