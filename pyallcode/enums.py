"""Common enums for device read indices and command codes.

These enums map to the integer arguments passed to various device
methods so you can use clear symbolic names instead of raw integers.

Use IntEnum so values can be passed anywhere an ``int`` is expected.
"""
from __future__ import annotations
from enum import IntEnum, unique


@unique
class Axis(IntEnum):
    """Axes for the accelerometer ``read_axis(index)`` method.

    Values:
        - X: 0
        - Y: 1
        - Z: 2
    """

    X = 0
    Y = 1
    Z = 2


@unique
class Button(IntEnum):
    """Indices for push buttons ``read(index)``.

    The driver defines 0 for left and 1 for right.
    """

    LEFT = 0
    RIGHT = 1

@unique
class Colour(IntEnum):
    """Indices for LCD colour.

    The driver defines the following indices:
        - White: 0
        - Black: 1
    """

    WHITE = 0
    BLACK = 1

@unique
class BitDepth(IntEnum):
    """Bit depths for CardRecordMic
    The driver defines the following indices:
        - BIT_8: 0
        - BIT_16: 1
    """
    BIT_8 = 0
    BIT_16 = 1

@unique
class SampleRate(IntEnum):
    """Sample rates for CardRecordMic
    The driver defines the following indices:
        - SR_8KHZ: 0
        - SR_16KHZ: 1
    """
    SR_8KHZ = 0
    SR_16KHZ = 1

@unique
class LineSensor(IntEnum):
    """Indices for line sensors ``read(index)``.

    The driver defines 0 for left and 1 for right.
    """

    LEFT = 0
    RIGHT = 1


@unique
class IRSensor(IntEnum):
    """Indices for IR distance sensors ``read(index)``.

    The driver defines the following indices:
        - LEFT: 0
        - FRONT_LEFT: 1
        - FRONT: 2
        - FRONT_RIGHT: 3
        - RIGHT: 4
        - BACK_RIGHT: 5
        - BACK: 6
        - BACK_LEFT: 7
    """

    LEFT = 0
    FRONT_LEFT = 1
    FRONT = 2
    FRONT_RIGHT = 3
    RIGHT = 4
    BACK_RIGHT = 5
    BACK = 6
    BACK_LEFT = 7

@unique
class ServoID(IntEnum):
    """Indices for Servo IDs.

    The driver defines the following indices:
        - SERVO_1: 1
        - SERVO_2: 2
        - SERVO_3: 3
        - SERVO_4: 4
    """

    SERVO_1 = 1
    SERVO_2 = 2
    SERVO_3 = 3
    SERVO_4 = 4 

__all__ = [
    "Axis",
    "Button",
    "Colour",
    "BitDepth",
    "SampleRate",
    "LineSensor",
    "IRSensor",
    "ServoID",
]
