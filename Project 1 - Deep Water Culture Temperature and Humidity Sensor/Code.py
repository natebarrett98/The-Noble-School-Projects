from machine import Pin
import time
import dht

sensor = dht.DHT11(Pin(15))

while True:
    sensor.measure()
    print("Temperature: {}°C   Humidity: {}% ".format(sensor.temperature(), sensor.humidity()))
    time.sleep(2)
