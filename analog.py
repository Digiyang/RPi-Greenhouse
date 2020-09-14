import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
 
# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 0
chan1 = AnalogIn(mcp, MCP.P0)
chan2 = AnalogIn(mcp, MCP.P1)
 
while True:
    print('Raw ADC Value (chan1): ', chan1.value)
    print('ADC Voltage (chan1): ' + str(chan1.voltage) + 'V')
    time.sleep(2)
    print('Raw ADC Value (chan2): ', chan2.value)
    print('ADC Voltage (chan2): ' + str(chan2.voltage) + 'v')
    time.sleep(2)
