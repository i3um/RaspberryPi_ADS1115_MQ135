import Adafruit_DHT

from flask import Flask,render_template,request
app = Flask(__name__)
sensor = Adafruit_DHT.DHT22
pin = '4'

@app.route("/")

def temp():

    hum,temp = Adafruit_DHT.read_retry(sensor, pin)


    return render_template('main.html',
                            hum = int(hum),
                            temp = int(temp))

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=80)
