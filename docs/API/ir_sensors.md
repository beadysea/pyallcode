# Module allcode.devices.ir_sensors

## class IRSensors

Methods:

### read(sensor: int) -> int

Reads the value of the given sensor.

Args:
>sensor (int): Number of sensor to read between 0 and 7

Raises:
>ValueError: when the sensor number is out of range.

Returns:
>int: the value of the given sensor.
