from allcode.enums import Servo
from allcode.serial_comms import CommunicationDevice


MIN_SERVO = 0
MIN_SERVO_POSITION = 0
MIN_SERVO_SPEED = 0
MAX_SERVO = 3
MAX_SERVO_POSITION = 256
MAX_SERVO_SPEED = 51


class Servos:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def enable(self, servo: Servo):
        """Enables the given servo motor.

        Args:
            servo (Servo): Enum of the servo to enable.
        """

        command = f'ServoEnable {servo.value}\n'
        self.device.send_message(command)

    def disable(self, servo: Servo):
        """Disable the given servo motor.

        Args:
            servo (Servo): Enum of the servo to disable.
        """

        command = f'ServoDisable {servo.value}\n'
        self.device.send_message(command)

    def set_position(self, servo: Servo, position: int):
        """Sets the given servo motor to the required position.

        Args:
            servo (Servo): Enum of the servo motor.
            position (int): the position of the servo between 0 and 255

        Raises:
            ValueError: when the servo position is out of range.
        """
        if position not in range(MIN_SERVO_POSITION, MAX_SERVO_POSITION):
            raise ValueError(
                f'Invalid position {position}. Position must be in the range {MIN_SERVO_POSITION} to {MAX_SERVO_POSITION-1}.')
        command = f'ServoSetPos {servo.value} {position}\n'
        self.device.send_message(command)

    def auto_move(self, servo: Servo, position: int):
        """Automatically moves the given servo motor to the required position.

        Args:
            servo (Servo): Enum of the servo motor.
            position (int): the position of the servo between 0 and 255

        Raises:
            ValueError: when the servo position is out of range.
        """
        if position not in range(MIN_SERVO_POSITION, MAX_SERVO_POSITION+1):
            raise ValueError(
                f'Invalid position {position}. Position must be in the range {MIN_SERVO_POSITION} to {MAX_SERVO_POSITION-1}.')
        command = f'ServoAutoMove {servo.value} {position}\n'
        self.device.send_message(command)

    def set_speed(self, servo: Servo, speed: int):
        """Sets the speed of the given servo motor.

        Args:
            servo (Servo): Enum of the servo motor
            speed (int): the speed of the servo between 0 and 50

        Raises:
            ValueError: _description_
        """
        if speed not in range(MIN_SERVO_SPEED,MAX_SERVO_SPEED):
            raise ValueError(
                f'Invalid speed {speed}. Speed must be in the range {MIN_SERVO_SPEED} to {MAX_SERVO_SPEED-1}.')
        command = f'ServoMoveSpeed {servo.value} {speed}\n'
        self.device.send_message(command)
