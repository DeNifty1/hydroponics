import RPi.GPIO as GPIO
import time
import Adafruit_DHT  # sudo pip3 install Adafruit_DHT
import logging

logging.basicConfig(filename='hydroponics.log', level=logging.INFO, format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%m/%d/%Y %I:%M%p')
# logging.basicConfig(level=logging.INFO, format='%(asctime)s|%(levelname)s|%(message)s', datefmt='%m/%d/%Y %I:%M%p')

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN  = 4

LIGHT_ON = [7]  # What hours in 24h format to turn on
LIGHT_OFF = [16]  # What hours in 24h format to turn off

PUMP_ON = [0,30]  # What minutes to turn on
PUMP_OFF = [10,40]  # What minutes to turn off,

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)  # Light
GPIO.setup(21, GPIO.OUT)  # Pump

# Intial state High is OFF ...LOW is ON
GPIO.output(20, GPIO.LOW)
GPIO.output(21, GPIO.LOW)

def get_temp_humidity():
    try:
        humidity, temperature_c = Adafruit_DHT.read_retry(DHT_SENSOR,DHT_PIN)
        #if humidity is not None and temperature_c is not None:
        #    logging.info("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature_c, humidity))
        #else:
        #    logging.error("Temp Sensor fail")
        # F Degrees
        temperature_f = (temperature_c * 9/5) + 32
        if humidity is not None and temperature_c is not None:
            logging.info("Temp={0:0.1f}F  Humidity={1:0.1f}%".format(temperature_f, humidity))
            print("Temp={0:0.1f}F  Humidity={1:0.1f}%".format(temperature_f, humidity))
        else:
            logging.error("Temp Sensor fail")
            print("Temp Sensor fail")
    except: 
        logging.error("Temp Code error occured")
        print("Temp Code error occured")
    
    
try:
    while True:
        #get_temp_humidity()
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min
        
        # Light code
        if hour in LIGHT_ON and minute == 0:
            GPIO.output(20, GPIO.LOW)
            logging.info('Light is ON')
            print('Light is ON')
        if hour in LIGHT_OFF and minute == 0:
            GPIO.output(20, GPIO.HIGH)
            logging.info('Light is OFF')
            print('Light is OFF')
        
        # Pump code
        if minute in PUMP_ON:
            GPIO.output(21, GPIO.LOW)
            logging.info('Pump is ON')
            print('Pump is ON')
        if minute in PUMP_OFF:
            GPIO.output(21, GPIO.HIGH)
            logging.info('Pump is OFF')
            print('Pump is OFF')
        
        time.sleep(55)
        
finally:
    GPIO.cleanup()