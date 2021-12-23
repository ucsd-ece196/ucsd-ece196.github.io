# Intro to Serial Communication
_Written by Curtis Lee_

## Motivation
* "UART vs SPI vs I2C" is common interview question
* Helps us connect multiple systems together
    * devices to microcontroller
    * microcontroller to computer

## Main types of Serial Communication
* SPI
    * Synchronous, has a clock pin
    * Need select/control pins to connect multiple devices
* I2C
    * Asynchronous, each device has address
* UART
    * Synchronous, devices need to agree on transfer speed, or baud rate
    * Usually bidirectional, and using two devices
  
In embedded development, both SPI and I2C are used mainly used for sensors, modules, etc and usually already integrated into pre-made libaries for those. 

UART is usually what people refer to as simply "serial", and is usually the go-to for connecting microcontroller systems together or connecting microcontrollers to a computer. Because of this, **in this tutorial we will focus mainly on UART**.

For more information on all the protocols and differences between them, check out [this article](https://www.seeedstudio.com/blog/2019/09/25/uart-vs-i2c-vs-spi-communication-protocols-and-uses/).

## How UART Serial works

### Basics

For bidirectional communication, UART is usually wired up in full-duplex mode like so:
![img/serial_uart_wiring.png](img/serial_uart_wiring.png)

On the sending device, each data byte is broken up and transmitted one bit at a time, with padding to detect when each bit starts, and sometimes extra bits for additional features. The data is then read and assembled back into bytes on the recieving device.
![img/serial_uart_waveform.png](img/serial_uart_waveform.png)

### Baud Rates

To ensure both devices can communicate with each other properly, they need to agree upon a fixed rate to send data, known as a **baud rate**. 

Since each of our bits are binary 0's and 1's, we can also consider baud rate equivalent to bit rate.

Some common baud rates:

* 9600
* 115200

### Encoding

By default, usually UART serial handles data in **bytes**. 

Bytes are really just 8-bit binary numbers, or 256 combinations of 1's and 0's, or 0-255 in decimal values.

To represent useful symbols like characters, some kind of encoding is needed. An encoding scheme maps these 0-255 binary values into symbols.

The most universal encoding scheme for bytes is [**ASCII**](https://www.ascii-code.com/). ASCII specifies which byte values correspond to a-z and A-Z letters, 0-9 digits, common punctuations marks, and some other features.


## How to use UART Serial

### Common USB-UART Adapters
There are some common cheap module boards out there that have Serial UART pins and accept a USB connection. Some are also built-in to cheap Arduino boards.

Usually they are based on one of these common chipsets. Some might require driver installation to work on some operating systems:

* Official Arduino Serial Chip
    * Built-in to most "official design" Arduino boards
    * Should "just work" on all systems
* FTDI FT232 Series
    * Most universlly compatible chipset, but also slightly more expensive
    * Should "just work" on all systems
* CH340 Series
    * [Drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers/all)
* PL2303 Series
    * [Drivers](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=225&pcid=41)
* CP2102 Series
    * [Drivers](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
* 

## Checking device connection

On the computer, there are some ways to check if the device is properly detected before doing anything. This is useful during troubleshooting.

### Windows

1. Open *Device Manager*
2. 

### Mac/Linux

ls /dev/*