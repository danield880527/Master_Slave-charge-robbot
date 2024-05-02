from gpiozero import MCP3008
import time

# 定義使用的 MCP3008 的 channel 號碼
ADC_CHANNEL = 0

# 建立 MCP3008 物件
adc = MCP3008(channel=ADC_CHANNEL)

try:
    while True:
        # 讀取 ADC 轉換後的數值
        raw_value = adc.value

        # 轉換成電壓值，假設使用 3.3V 的供電電壓
        voltage = raw_value * 3.3

        # 顯示測量值
        print("ADC Raw Value: {:.4f}, Voltage: {:.2f} V".format(raw_value, voltage))

        # 等待一段時間
        time.sleep(0.5)

except KeyboardInterrupt:
    # 結束程式時，釋放 gpio 資源
    adc.close()