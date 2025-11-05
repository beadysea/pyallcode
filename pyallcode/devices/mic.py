"""Module for interacting with the microphone level sensor."""
from ..comm.connection import Connection
from .base import DeviceBase


class Mic(DeviceBase):
    """Represents the microphone level sensor.
    

    Attributes:
        conn (Connection): The connection to the robot.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the Mic sensor with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def read(self) -> int:
        """Reads the microphone level.

        Returns:
            int: The microphone level (0-100) or -1 on error.
        """
        return int(self.conn.execute('ReadMic') or -1)
