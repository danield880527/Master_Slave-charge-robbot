import RPi.GPIO as GPIO
import time
import sendemail2 

GPIO.setmode(GPIO.BCM)
PIR_PIN = 26  
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("derection start")
    time.sleep(1)
    while True:
        val = gpio.input(PIR_PIN)
        print(val)
        if val == True:
            print("Motion Detected!")
            sendemail2.sendemail()  
            time.sleep(5)  
            #GPIO.cleanup(PIR_PIN)
        else:
            print('notthing')
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
    a
