import RPi.GPIO as GPIO
import sys
import time
import Adafruit_DHT

yellow = 18
blue = 22
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

sensor = Adafruit_DHT.DHT22
pin = 4
temp = 0
humi = 0

while True:
  humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
  if humidity is not None and temperature is not None:
	print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	if temp != temperature and humi != humidity:
            GPIO.output(yellow,GPIO.HIGH)
            GPIO.output(blue,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(yellow,GPIO.LOW)
            GPIO.output(blue,GPIO.LOW)
            temp = temperature
            humi = humidity
        else:
            if temp != temperature:
                GPIO.output(yellow,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(yellow,GPIO.LOW)
                temp = temperature
            if humi != humidity:
                GPIO.output(blue,GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(blue,GPIO.LOW)
                humi = humidity
        
        time.sleep(2)
  else:
	print 'Cannot Reading'
