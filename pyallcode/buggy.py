"""Matrix TSL Buggy API."""

from .devices.axis import Axes
from .devices.buttons import Buttons
from .devices.ir_sensors import IRSensors
from .devices.lcd import LCD
from .devices.leds import LEDs
from .devices.light_sensor import LightSensor
from .devices.line_sensors import LineSensors
from .devices.mic import Mic
from .devices.sd_card import SDCard
from .devices.servos import Servos
from .devices.speaker import Speaker
from .serial_comms import CommunicationDevice

# MAX and MIN Constants
MIN_ANGLE = 0
MAX_ANGLE = 360
MIN_DISTANCE = 0
MAX_DISTANCE = 1000
MIN_SPEED = -100
MAX_SPEED = 100


class Buggy:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device
        self.axis = Axes(self.device)
        self.buttons = Buttons(self.device)
        self.ir_sensors = IRSensors(self.device)
        self.lcd = LCD(self.device)
        self.leds = LEDs(self.device)
        self.light_sensor = LightSensor(self.device)
        self.line_sensors = LineSensors(self.device)
        self.mic = Mic(self.device)
        self.sd_card = SDCard(self.device)
        self.servos = Servos(self.device)
        self.speaker = Speaker(self.device)

    # system methods

    def api_version(self):
        """Returns the API version of the allcode buggy"""
        command = "GetAPIVersion\n"
        return self.device.send_message(command)

    def battery_voltage(self) -> float:
        """Returns the battery voltage."""
        command = "GetBattery\n"
        value = self.device.send_message(command)
        return value / 100

    # motor methods
    def forward(self, distance: int) -> None:
        """Moves the buggy forward by the given distance.

        Args:
            distance (int): distance between 0 and 1000 mm

        Raises:
            ValueError: when distance is out of range
        """
        if distance < MIN_DISTANCE or distance > MAX_DISTANCE:
            raise ValueError(
                f"Invalid distance {distance}mm. Distance must be between {MIN_DISTANCE} and {MAX_DISTANCE} mm"
            )
        command = f"Forwards {distance}\n"
        self.device.send_message(command)

    def backward(self, distance: int) -> None:
        """Moves the buggy backward by the given distance.

        Args:
            distance (int): distance between 0 and 1000 mm

        Raises:
            ValueError: when distance is out of range.
        """
        if distance < MIN_DISTANCE or distance > MAX_DISTANCE:
            raise ValueError(
                f"Invalid distance {distance}mm. Distance must be between {MIN_DISTANCE} and {MAX_DISTANCE} mm"
            )
        command = f"Backwards {distance}\n"
        self.device.send_message(command)

    def left(self, angle: int) -> None:
        """Turns the buggy left by the given angle.

        Args:
            angle (int): angle between 0 and 360 degrees.

        Raises:
            ValueError: when angle is out of range.
        """
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            raise ValueError(
                f"Invalid angle {angle} degrees. Angle must be between {MIN_ANGLE} and {MAX_ANGLE} degrees"
            )
        command = f"Left {angle}\n"
        self.device.send_message(command)

    def right(self, angle: int) -> None:
        """Turns the buggy right by the given angle.

        Args:
            angle (int): angle between 0 and 360 degrees.

        Raises:
            ValueError: when angle is out of range.
        """
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            raise ValueError(
                f"Invalid angle {angle} degrees. Angle must be between {MIN_ANGLE} and {MAX_ANGLE} degrees"
            )
        command = f"Right {angle}\n"
        self.device.send_message(command)

    def set_motor_speeds(self, left_speed: int, right_speed: int) -> None:
        """Independently sets the speed of the left and right motors.

        Args:
            left_speed (int): speed between -100 and 100.
            right_speed (int): speed between -100 and 100.

        Raises:
            ValueError: when left or right speed is out of range.
        """
        if left_speed < MIN_SPEED or left_speed > MAX_SPEED:
            raise ValueError(
                f"Invalid left_speed {left_speed}. Left speed must be between {MIN_SPEED} and {MAX_SPEED} m/s"
            )
        if right_speed < MIN_SPEED or right_speed > MAX_SPEED:
            raise ValueError(
                f"Invalid right_speed {right_speed}. Right speed must be between {MIN_SPEED} and {MAX_SPEED} degrees"
            )

        command = f"SetMotors {left_speed} {right_speed}\n"
        self.device.send_message(command)
