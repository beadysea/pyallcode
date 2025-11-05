"""Module for interacting with the accelerometer device."""
from ..comm.connection import Connection
from .base import DeviceBase


class Accelerometer(DeviceBase):
    """Represents the accelerometer. Provides axis reads by index or helpers.
    
    Args:
        conn (Connection): The connection to use for communication.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the Accelerometer with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def read_axis(self, index: int) -> int:
        """Reads the accelerometer value for the specified axis index.
        
        Args:
            index (int): The axis index (0 for X, 1 for Y, 2 for Z).
            
            Returns:
                int: The accelerometer value for the specified axis.
        """
        return int(self.conn.execute(f'ReadAxis {int(index)}') or -1)

    # Convenience helpers
    def x(self) -> int:
        """Reads the accelerometer value for the X axis."""
        return self.read_axis(0)

    def y(self) -> int:
        """Reads the accelerometer value for the Y axis."""
        return self.read_axis(1)

    def z(self) -> int:
        """Reads the accelerometer value for the Z axis."""
        return self.read_axis(2)
