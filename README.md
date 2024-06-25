# Allcode API

The Allcode API is a python library of methods used to control Matrix Tsl allcode devices over a bluetooth serial connection. Based on the original formula allcode api provded by Matrix Tsl, this library has been redesigned from the ground up.

* Automatic detection of available serial port
* Null device for testng without a serial device connected.
* Improved separation of responsibilities

## Hardware Requirements

The current version of the api requires a [Formula Allcode](https://www.matrixtsl.com/allcode/formula/) robot buggy available from Matrix Tsl.

## Using the Allcode API

Basic Allcode Buggy functions example

```Python
import time
from allcode import buggy, serial_comms

car = buggy.Buggy(serial_comms.SerialDevice)
car.forward(500)
car.left(30)
car.backward(300)
car.right(60)
car.set_motor_speeds(100,-100)
time.sleep(2)
car.set_motor_speeds(0,0)
```

The buggy has several peripheral devices, each of which are seperate objects.

Avaiable devices

* axis - 3 axis accelerometer sensor
* button
* infrared sensors
* lcd
* leds
* light sensor
* line sensors
* microphone
* sd card
* servos
* loudspeaker

```Python
import time
from allcode import buggy, serial_comms

car = buggy.Buggy(serial_comms.SerialDevice)
# switching all 8 leds on
car.leds.write(255)
# switching led 5 off
car.leds.off(5)
# switching all 8 leds off
car.leds.write(0)
```
