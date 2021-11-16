import adafruit_dht
import board
import time

# Setup DHT Sensor.
# Can change pin or DHT type if needed.
dht_sensor = adafruit_dht.DHT22(board.D4)

while True:
    try:
        # Read the data
        temp = dht_sensor.temperature
        hum = dht_sensor.humidity
    except RuntimeError as error: 
        # Handle routine errors.
        # The sensor is pretty derpy and often doesn't output properly.
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        # Handle other errors.
        dht_sensor.exit()
        raise error

    # print to console
    print("Temperature =", temp, 'C')
    print("Humidity =", hum, '%')

    # run every 5 seconds
    time.sleep( 5 )