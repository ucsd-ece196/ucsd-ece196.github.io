import serial
import time

arduino = serial.Serial(port='/dev/ttyUSB1', baudrate=9600, timeout=0.1)

while True:
    tx_data = input("Enter something: ") # Taking input from user
    arduino.write(bytes(tx_data, 'utf-8')) # need to encode utf-8 into ascii
    rx_data = arduino.readline()
    print(rx_data) # printing the value