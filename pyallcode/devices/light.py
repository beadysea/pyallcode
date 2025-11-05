"""Module for interacting with the ambient light sensor."""
from ..comm.connection import Connection
from .base import DeviceBase


class LightSensor(DeviceBase):
    """Represents the ambient light sensor (no index).
    Args:
        conn (Connection): The connection to the device.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the LightSensor with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def read(self) -> int:
        """Reads the value from the light sensor.
        Returns:
            int: The light sensor value.
        """
        return int(self.conn.execute('ReadLight') or -1)
