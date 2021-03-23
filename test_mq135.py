import time, signal, sys
from Adafruit_ADS1x15 import ADS1x15

voltVector = []
def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
    
ADS1115 = 0x01
gain = 4096 
adc3 = ADS1x15.ADS1115()

while (True):
   volts = adc3.read_adc(0, 1, 250) / 1000
   #print("MQ-135 %.6fv" % volts)
   voltVector.append(volts)
   time.sleep(1)
   print(*voltVector, sep = '\n')
