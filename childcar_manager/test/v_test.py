from gpiozero import MCP3008
import time

sensor1 = MCP3008(0)
sensor2 = MCP3008(1)

for i in range(100):
    print("sensor1:{}, sensor2:{}".format(sensor1.value, sensor2.value))
    time.sleep(0.5)
