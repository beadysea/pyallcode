"""Module for interacting with the IR distance sensors."""
from ..comm.connection import Connection
from .base import DeviceBase


class IRSensors(DeviceBase):
    """Represents one IR distance sensor (index 0..7).
    
    Args:
        conn (Connection): The connection to the device.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the IRSensors with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def read(self, index: int) -> int:
        """Reads the value from the specified IR sensor.
        
        Args:
            index (int): The sensor index (0-7).
            
        Returns:
            int: The sensor value.
        """
        return int(self.conn.execute(f'ReadIR {index}') or -1)
