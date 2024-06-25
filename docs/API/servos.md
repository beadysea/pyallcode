# Module allcode.devices.servos

## class Servos

### enable(self, servo: Servo)

Enables the given servo motor.

Args:
>servo (Servo): Enum of the servo to enable.

### disable(self, servo: Servo)

Disable the given servo motor.

Args:
>servo (Servo): Enum of the servo to disable.

### set_position(self, servo: Servo, position: int)

Sets the given servo motor to the required position.

Args:
>servo (Servo): Enum of the servo motor.
>
>position (int): the position of the servo between 0 and 255

Raises:
>ValueError: when the servo position is out of range.

### auto_move(self, servo: Servo, position: int)

Automatically moves the given servo motor to the required position.

Args:
>servo (Servo): Enum of the servo motor.
>
>position (int): the position of the servo between 0 and 255

Raises:
>ValueError: when the servo position is out of range.

### set_speed(self, servo: Servo, speed: int)

Sets the speed of the given servo motor.

Args:
>servo (Servo): Enum of the servo motor
>
>speed (int): the speed of the servo between 0 and 50

Raises:
>ValueError: when the servo speed is out of range.
