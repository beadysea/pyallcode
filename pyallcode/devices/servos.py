"""Module for interacting with the servo motors."""
from ..comm.connection import Connection
from .base import DeviceBase

class Servos(DeviceBase):
    """Represents the servo motors.
    Args:
        conn (Connection): The connection to the device.
    """
    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the Servos with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def enable(self, index: int) -> None:
        """Enable the specified servo motor.
        
        Args:
            index (int): The index of the servo motor to enable.
        """
        self.conn.execute(f'ServoEnable {int(index)}', expect_response=False)

    def disable(self, index: int) -> None:
        """Disable the specified servo motor.
        Args:
            index (int): The index of the servo motor to disable.
        """
        self.conn.execute(f'ServoDisable {int(index)}', expect_response=False)

    def set_pos(self, index: int, position: int) -> None:
        """Set the position of the specified servo motor.
        Args:
            index (int): The index of the servo motor to set.
            position (int): The position to set the servo motor to.
        """
        self.conn.execute(f'ServoSetPos {int(index)} {int(position)}', expect_response=False)

    def auto_move(self, index: int, position: int) -> None:
        """Move the specified servo motor to the desired position automatically.
        Args:
            index (int): The index of the servo motor to move.
            position (int): The position to move the servo motor to.
        """
        self.conn.execute(f'ServoAutoMove {int(index)} {int(position)}', expect_response=False)

    def move_speed(self, speed: int) -> None:
        """Set the speed of the specified servo motor.
        Args:
            speed (int): The speed to set the servo motor to.
        """
        self.conn.execute(f'ServoMoveSpeed {int(speed)}', expect_response=False)
