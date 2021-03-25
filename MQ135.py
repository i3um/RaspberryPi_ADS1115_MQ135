import time
from MQ135 import MQ135
from Adafruit_ADS1x15 import ADS1x15

class mq135lib_example(object):
    """MQ135 lib example"""
    

    def __init__(self, pin, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.mq135 = MQ135() # analog PIN

    def pprint(self):
        """Continuos print of MQ135 values """

        while True:
            ad3 = ADS1x15.ADS1115()
            pin = 0
            rzero = self.mq135.get_rzero(ad3)
            corrected_rzero = self.mq135.get_corrected_rzero(self.temperature, self.humidity, ad3)
            resistance = self.mq135.get_resistance(ad3, pin)
            ppm = self.mq135.get_ppm(ad3, pin)
            corrected_ppm = self.mq135.get_corrected_ppm(self.temperature, self.humidity, ad3)

            print("MQ135 RZero: " + str(rzero) +"\t Corrected RZero: "+ str(corrected_rzero)+
                  "\t Resistance: "+ str(resistance) +"\t PPM: "+str(ppm)+
                  "\t Corrected PPM: "+str(corrected_ppm)+"ppm")
            time.sleep(0.3)

if __name__ == "__main__":
    mq = mq135lib_example(0, 21.0, 25.0)
    mq.pprint()
