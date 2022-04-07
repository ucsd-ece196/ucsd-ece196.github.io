import serial
import time
arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=0.1)

while True:
    rx_data = arduino.readline()
    if rx_data:
        print(rx_data) # printing the value
        if rx_data == b'x':
            print('Button was pressed !')
    time.sleep(0.01)
