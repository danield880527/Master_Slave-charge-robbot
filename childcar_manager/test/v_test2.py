import mcp3008
import time

try:
    while True:
        adc = mcp3008.MCP3008()
        print(adc.read([mcp3008.CH1]))  # prints raw data [CH0]
        adc.close()
        time.sleep(0.5)

except Exception as e:
    print(str(e))
