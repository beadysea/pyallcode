from enum import Enum


class Axis(Enum):
    """Enum of axis"""

    X = 0
    Y = 1
    Z = 2


class Button(Enum):
    """Enum of buttons."""

    LEFT = 0
    RIGHT = 1


class Colour(Enum):
    """Enum of colours"""

    WHITE = 0
    BLACK = 1


class IRSensor(Enum):
    """Enum of IR sensors"""

    LEFT = 0
    FRONT_LEFT = 1
    FRONT = 2
    FRONT_RIGHT = 3
    RIGHT = 4
    REAR_RIGHT = 5
    REAR = 6
    REAR_LEFT = 7


class LineSensor(Enum):
    """Enum of line sensors"""

    LEFT = 0
    RIGHT = 1


class BitDepth(Enum):
    """Enum of bit depths"""

    B_8 = 0
    B_16 = 1


class SampleRate(Enum):
    """Enum of sample rates"""

    F_8K = 0
    F_16K = 1


class Servo(Enum):
    """Enum of servos"""

    ONE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
