import RPi.GPIO as GPIO
import time
import sys

AO_pin = 0
A1_pin = 1
# flame sensor AO connected to ADC chanannel 0
# change these as desired - they're the pins connected from the
# SPI port on the ADC to the Cobbler
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8

S1 = 17
S4 = 21
K1 = 23

# port init


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    # set up the SPI interface pins
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)

    GPIO.setup(S1, GPIO.OUT)
    GPIO.setup(S4, GPIO.OUT)
    GPIO.setup(K1, GPIO.OUT)
    pass

# read SPI data from MCP3008(or MCP3204) chip,8 possible adc's (0 thru 7)


def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin, False)  # start clock low
    GPIO.output(cspin, False)     # bring CS low

    commandout = adcnum
    commandout |= 0x18  # start bit + single-ended bit
    commandout <<= 3    # we only need to send 5 bits here
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)

    adcout = 0
    # read in one empty bit, one null bit and 10 ADC bits
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1

    GPIO.output(cspin, True)

    adcout >>= 1       # first bit is 'null' so drop it
    return adcout


def main():
    init()
    time.sleep(2)
    print("will detect voltage")
    while True:
        ad_value = readadc(AO_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
        voltage = ad_value*(4.88/1024)*5

        ad2_value = readadc(A1_pin, SPICLK, SPIMOSI, SPIMISO, SPICS)
        charge_voltage = ad2_value*(4.88/1024)*5
        charge_current = charge_voltage/1500  # this is R

        print("***********")
        print(" Voltage is: " + str("%.2f" % voltage)+"V")
        print(" Charge Voltage is: " + str("%0.2f" % charge_voltage)+"v")
        print(" Charge Current is: " + str("%0.2f" % charge_current)+"A")
        print("***********")
        print(' ')
        time.sleep(0.5)
        # if 5 < voltage < 8 : #need fix num or add time sleep + if
        #     GPIO.output(S1, GPIO.LOW)
        #     GPIO.output(K1, GPIO.HIGH)
        #     print("S1 on,state:B,link completed NOT ready to charge")
        #     time.sleep(2)

        # elif 0 <= voltage < 1:
        #     GPIO.output(S1, GPIO.HIGH)
        #     GPIO.output(K1, GPIO.HIGH)
        #     print("not open 12v")

        # elif 10 < voltage < 12:
        #     GPIO.output(S1, GPIO.HIGH)
        #     GPIO.output(K1, GPIO.HIGH)
        #     print("S1 off,state:A,NOT link completed")
        #     print("charge defeat")

        # elif 1 < voltage < 3:
        #     GPIO.output(S1, GPIO.LOW)
        #     print("on,state:D,link completed ready to charge")
        #     time.sleep(2)
        #     if GPIO.input(S1) == GPIO.LOW:
        #         GPIO.output(K1, GPIO.LOW)
        #         print('k1 close,start charge')
        # else:
        #     GPIO.output(S1, GPIO.HIGH)
        #     GPIO.output(K1, GPIO.HIGH)
        #     #print("off,state:A,NOT link completed")
        #     #print("charge defeat")
        #     print('error')
        #     print('exit program')
        #     sys.exit()
        #     #time.sleep(2)

        if 10 < voltage < 13:
            #GPIO.output(S1, GPIO.LOW)
            #GPIO.output(K1, GPIO.LOW)
            print("off,state:A,NOT link completed")
            time.sleep(2)
            link_voltage = voltage
            if 5 < link_voltage < 8:
                GPIO.output(S1, GPIO.LOW)
                GPIO.output(K1, GPIO.HIGH)
                print("S1 on,state:B,link completed NOT ready to charge")
                time.sleep(2)

                if 1 < voltage < 3:
                    GPIO.output(S1, GPIO.LOW)
                    print("on,state:D,link completed ready to charge")
                    time.sleep(2)

                    if GPIO.input(S1) == GPIO.LOW:
                        GPIO.output(K1, GPIO.LOW)
                        print('k1 close,start charge')

                        if charge_voltage > 16:
                            print("charge voltage is too hight")
                            sys.exit
                        else:
                            print("normal charge")

                else:
                    print("state D error")
            else:
                print("state B error")
        else:
            GPIO.output(S1, GPIO.HIGH)
            GPIO.output(K1, GPIO.HIGH)
            print("12v is not open")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
GPIO.cleanup()
