"""Module for interacting with the push buttons device."""
from ..comm.connection import Connection
from .base import DeviceBase

class PushButtons(DeviceBase):
    """Represents the digital push buttons (0: left, 1: right).
    
    Args:
        conn (Connection): The connection to the device.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the PushButtons with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def read(self, index: int) -> bool:
        """Reads the state of the specified push button.

        Args:
            index (int): The button index (0 for left, 1 for right).

        Returns:
            bool: True if pressed, False otherwise.
        """
        value = self.conn.execute(f'ReadSwitch {index}')
        # Treat any non-zero truthy integer as pressed
        try:
            return bool(int(value))
        except Exception:
            return False
