"""Matrix TSL robot API."""

from .devices.axis import Axes
from .devices.push_buttons import PushButtons
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


class Robot:
    """_summary_"""

    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device
        self.axis = Axes(self.device)
        self.push_buttons = PushButtons(self.device)
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
        """Returns the API version of the allcode robot."""
        return self.device.send_message("GetAPIVersion\n")

    def battery_voltage(self) -> float:
        """Returns the battery voltage."""
        value: int = self.device.send_message("GetBattery\n")
        return value / 100

    # motor methods
    def forward(self, distance: int) -> None:
        """Moves the robot forward by the given distance.

        Args:
            distance: distance between 0 and 1000 mm

        Raises:
            ValueError: when distance is out of range
        """
        if distance < MIN_DISTANCE or distance > MAX_DISTANCE:
            raise ValueError(
                f"Invalid distance {distance}mm. Distance must be between {MIN_DISTANCE} and {MAX_DISTANCE} mm"
            )
        self.device.send_message(f"Forwards {distance}\n")

    def backward(self, distance: int) -> None:
        """Moves the robot backward by the given distance.

        Args:
            distance (int): distance between 0 and 1000 mm

        Raises:
            ValueError: when distance is out of range.
        """
        if distance < MIN_DISTANCE or distance > MAX_DISTANCE:
            raise ValueError(
                f"Invalid distance {distance}mm. Distance must be between {MIN_DISTANCE} and {MAX_DISTANCE} mm"
            )
        self.device.send_message(f"Backwards {distance}\n")

    def left(self, angle: int) -> None:
        """Turns the robot left by the given angle.

        Args:
            angle: angle between 0 and 360 degrees.

        Raises:
            ValueError: when angle is out of range.
        """
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            raise ValueError(
                f"Invalid angle {angle} degrees. Angle must be between {MIN_ANGLE} and {MAX_ANGLE} degrees"
            )
        self.device.send_message(f"Left {angle}\n")

    def right(self, angle: int) -> None:
        """Turns the robot right by the given angle.

        Args:
            angle (int): angle between 0 and 360 degrees.

        Raises:
            ValueError: when angle is out of range.
        """
        if angle < MIN_ANGLE or angle > MAX_ANGLE:
            raise ValueError(
                f"Invalid angle {angle} degrees. Angle must be between {MIN_ANGLE} and {MAX_ANGLE} degrees"
            )
        self.device.send_message(f"Right {angle}\n")

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

        self.device.send_message(f"SetMotors {left_speed} {right_speed}\n")
