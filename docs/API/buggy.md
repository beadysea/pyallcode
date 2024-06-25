# The Allcode API v2.0.0

The allcode API provides a Python interface to all the methods available to control
the formula allcode buggy. The package is organised into the following:

- allcode. Contains the buggy and enums modules.
- allcode.devices. Contains all the peripheral device modules.

This API documentation details all the methods available in each module.

## allcode.buggy

Use the Buggy in your own code as follows:

```Python
from allcode.buggy import Buggy
from allcode.serial_comms import SerialDevice

def main():
    car = Buggy(SerialDevice()) 
```

The Buggy has the following methods. To access a method use the . operator, for example:

```Python
api_version = car.api_version()
voltage = car.battery_voltage()
car.forward(100)
car.backward(200)
car.left(45)
car.right(60)
```

### api_version() -> int

Returns the API version of the allcode buggy

### battery_voltage() -> float

Returns the battery voltage.

### forward(distance: int)

Moves the buggy forward by the given distance.

Args:

> distance (int): distance between 0 and 1000 mm

Raises:

>ValueError: when distance is out of range

### backward(distance: int)

Moves the buggy backward by the given distance.

Args:
> distance (int): distance between 0 and 1000 mm

Raises:
> ValueError: when distance is out of range.

### left(angle: int)

Turns the buggy left by the given angle.

Args:
> angle (int): angle between 0 and 360 degrees.

Raises:
> ValueError: when angle is out of range.

### right(angle: int)

Turns the buggy right by the given angle.

Args:
> angle (int): angle between 0 and 360 degrees.

Raises:
> ValueError: when angle is out of range.

### set_motor_speeds(left: int, right: int)

Independently sets the speed of the left and right motors.

Args:
> left_speed (int): speed between -100 and 100.
> right_speed (int): speed between -100 and 100.

Raises:
> ValueError: when left or right speed is out of range.
