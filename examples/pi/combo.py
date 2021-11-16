import adafruit_dht
import board
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)

dht_pin = board.D4
dht_sensor = adafruit_dht.DHT11(dht_pin, use_pulseio=False)

def callback_func(*args):
    print("Button was pushed!")
    while True:
        try:
            GPIO.output( 17, GPIO.HIGH )
            temp_c = dht_sensor.temperature
            temp_f = temp_c * (9 / 5) + 32
            hum = dht_sensor.humidity
            print("Temperature =", temp_c, 'C,', temp_f, 'F')
            print("Humidity =", hum, '%')
            time.sleep( 0.5 )
            GPIO.output( 17, GPIO.LOW )
            break
        except:
            print('error reading, trying again...')
            continue

GPIO.add_event_detect(10, edge=GPIO.FALLING, callback=callback_func, bouncetime=200)

input("press enter 2 quit\n") # block program from exiting





