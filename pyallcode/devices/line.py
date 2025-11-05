"""Module for interacting with the line sensors."""
from ..comm.connection import Connection
from .base import DeviceBase


class LineSensors(DeviceBase):
    """Represents a line sensor (index 0..1)."""

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def read(self, index: int) -> bool:
        """Reads the value from the specified line sensor.

        Args:
            index (int): The sensor index (0-1).

        Returns:
            bool: True when the sensor reads line present (non-zero), False otherwise.
        """
        value = self.conn.execute(f'ReadLine {index}')
        try:
            return bool(int(value))
        except Exception:
            return False
