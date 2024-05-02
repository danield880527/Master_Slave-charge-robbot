import pigpio
pi = pigpio.pi()
pi.set_PWM_frequency(18, 400)  # 设定18号引脚产生的pwm波形的频率为400Hz
pi.set_PWM_range(18, 2000)
# 指定要把18号引脚上的一个pwm周期分成多少份，这里是分成2000份，这个数据的范围是25-40000
pi.set_PWM_dutycycle(18, 200)  # 指定pwm波形的占空比，这里的占空比为200/2000,2000是上一个函数设定的
