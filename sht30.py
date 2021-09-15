import RPi.GPIO as GPIO
import time
import Adafruit_DHT  # sudo pip3 install Adafruit_DHT
import logging
import smbus

bus = smbus.SMBus(1)

bus.write_i2c_block_data(0x44,0x2C, [0x06])

time.sleep(1)
data = bus.read_i2c_block_data(0x44,0x00, 6)
 
print(data[0])
print(data[1])
print(data[2])
print(data[3])
print(data[4])
print(data[5])

temp = data[0] * 256 + data[1]
print(temp)
cTemp = -45 + (175 * temp / 65535.0)
fTemp = -49 + (315 * temp / 65535.0)
humidity =  100 * (data[3] *256 + data[4]) / 65535.0

print("Celsius: %.2f C" %cTemp)
print("Fahrenheit: %.2f F" %fTemp)
print("Humidity: %.2f %%RH" %humidity)


