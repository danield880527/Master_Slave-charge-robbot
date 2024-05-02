import pigpio
import time
pi = pigpio.pi()
gpio=12
gpio2=13
#pi.set_PWM_frequency(gpio,400000000)
pi.hardware_PWM(gpio,19000,500000)
pi.set_PWM_range(gpio,100)     
pi.set_PWM_dutycycle(gpio,50)  #duti ratio
print('frequencypi',pi.get_PWM_frequency(gpio),'Hz')
print('dutycycle:',pi.get_PWM_dutycycle(gpio),'%')

pi.set_PWM_frequency(gpio2,30)
pi.set_PWM_range(gpio2,100)     
pi.set_PWM_dutycycle(gpio2,50)  #duti ratio
print('frequencypi2',pi.get_PWM_frequency(gpio2),'Hz')
print('dutycycle2:',pi.get_PWM_dutycycle(gpio2),'%')


time.sleep(5)
#GPIO.cleanup()

pi.stop
print('ok')
