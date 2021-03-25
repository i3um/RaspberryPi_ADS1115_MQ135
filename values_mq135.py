import time, signal, sys, math 
from Adafruit_ADS1x15 import ADS1x15


class MQ135(object):
    voltVector = []
    RLOAD = 10.0
    RZERO = 76.63
    PARA = 116.6020682

    PARB = 2.769034857
    CORA = 0.00035
    CORB = 0.02718
    CORC = 1.39538
    CORD = 0.0018
    CORE = -0.003333333
    CORF = -0.001923077
    CORG = 1.130128205
    ATMOCO2 = 397.13




    ADS1115 = 0x01
    gain = 4096
    ad3 = ADS1x15.ADS1115()
    pin = 0


    def get_correction_factor(self, temperature, humidity):
        return self.CORE * temperature + self.CORF * humidity + self.CORG


    def get_resistance(self, ad3, pin):
        a = ad3.read_adc(0, 1, 250) / 1000
        return (1023./a - 1.) * self.RLOAD


    def get_corrected_resistance(self, temperature, humidity, ad3):
        return self.get_resistance(ad3, 0) / self.get_correction_factor(temperature, humidity)


    def get_ppm(self, ad3, pin):
        return self.PARA * math.pow((self.get_resistance(ad3, pin) / self.RZERO), -self.PARB)


    def get_corrected_ppm(self, temperature, humidity, ad3):
        return self.PARA * math.pow((self.get_corrected_resistance(temperature, humidity, ad3) / self.RZERO), -self.PARB)


    def get_rzero(self, ad3):
        return self.get_resistance(ad3, 0) * math.pow((self.ATMOCO2 / self.PARA), (1. / self.PARB))


    def get_corrected_rzero(self, temperature, humidity, ad3):
        return self.get_corrected_resistance(temperature, humidity, ad3) * math.pow((self.ATMOCO2 / self.PARA), (1. / self.PARB))

def mq135lib_example():
    temperature = 21.0
    humidity = 25.0

    ad3 = ADS1x15.ADS1115()
    mq135 = MQ135()
    pin = 0

    while (True):
        rzero = mq135.get_rzero(ad3)
        corrected_rzero = mq135.get_corrected_rzero(temperature, humidity, ad3)
        resistance = mq135.get_resistance(ad3, pin)
        ppm = mq135.get_ppm(ad3, pin)
        corrected_ppm = mq135.get_corrected_ppm(temperature, humidity, ad3)
        print("MQ135 RZero: " + str(rzero) + "\t Corrected RZero: " + str(corrected_rzero) +
              "\t Resistance: " + str(resistance) + "\t PPM: " + str(ppm) +
              "\t Corrected PPM: " + str(corrected_ppm) + "ppm", sep = '\n')
        time.sleep(0.3)


if __name__ == "__main__":
    mq135lib_example()
