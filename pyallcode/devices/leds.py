"""Module for interacting with the device's LEDs."""
from ..comm.connection import Connection
from .base import DeviceBase

class LEDs(DeviceBase):
    """Represents the device's LEDs.

    Args:
        conn (Connection): The connection to the device.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the LEDs with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def write(self, value: int) -> None:
        """Writes a value to the LEDs.
        Args:
            value (int): The value to write (0-255).
        """
        self.conn.execute(f'LEDWrite {int(value)}', expect_response=False)

    def on(self, index: int) -> None:
        """Turns on the specified LED.
        Args:
            index (int): The index of the LED to turn on.
        """
        self.conn.execute(f'LEDOn {int(index)}', expect_response=False)

    def off(self, index: int) -> None:
        """Turns off the specified LED.
        Args:
            index (int): The index of the LED to turn off.
        """
        self.conn.execute(f'LEDOff {int(index)}', expect_response=False)
