import RPi.GPIO as GPIO
from time import sleep
import Adafruit_MCP3008

adc = Adafruit_MCP3008.MCP3008(clk = 23, cs = 24, mosi = 19, miso = 21)

while True:
    moisture = adc.read_adc(0)
    if moisture >= 930:
        print("Water me please!")
    elif moisture < 930 and moisture >= 350:
        print("I have enough water!")
    elif moisture < 350 :
        print("Too much water!")
    sleep(2)
