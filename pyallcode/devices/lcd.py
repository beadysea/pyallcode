"""Module for interacting with the LCD display."""
from ..comm.connection import Connection
from .base import DeviceBase

class LCD(DeviceBase):
    """Represents the LCD display.
    
    Args:
        conn (Connection): The connection to the device.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the LCD with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def clear(self) -> None:
        """Clears the LCD display."""
        self.conn.execute('LCDClear', expect_response=False)

    def print(self, x: int, y: int, text: str) -> None:
        """Prints text on the LCD display at the specified coordinates.
        
        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            text (str): The text to print.
        """
        self.conn.execute(f'LCDPrint {int(x)} {int(y)} {text}', expect_response=False)

    def number(self, x: int, y: int, value: int) -> None:
        """Displays a number on the LCD at the specified coordinates.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            value (int): The number to display.
        """
        self.conn.execute(f'LCDNumber {int(x)} {int(y)} {int(value)}', expect_response=False)

    def pixel(self, x: int, y: int, state: int) -> None:
        """Sets the state of a pixel on the LCD.
        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            state (int): The pixel state (1 for on, 0 for off).
        """
        self.conn.execute(f'LCDPixel {int(x)} {int(y)} {int(state)}', expect_response=False)

    def line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Draws a line on the LCD.
        Args:
            x1 (int): The starting x-coordinate.
            y1 (int): The starting y-coordinate.
            x2 (int): The ending x-coordinate.
            y2 (int): The ending y-coordinate.
        """
        self.conn.execute(f'LCDLine {int(x1)} {int(y1)} {int(x2)} {int(y2)}', expect_response=False)

    def rect(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Draws a rectangle on the LCD.
        Args:
            x1 (int): The top-left x-coordinate.
            y1 (int): The top-left y-coordinate.
            x2 (int): The bottom-right x-coordinate.
            y2 (int): The bottom-right y-coordinate.
        """
        self.conn.execute(f'LCDRect {int(x1)} {int(y1)} {int(x2)} {int(y2)}', expect_response=False)

    def backlight(self, value: int) -> None:
        """Sets the backlight of the LCD.
        Args:
            value (int): The backlight value (1 for on, 0 for off).
        """
        self.conn.execute(f'LCDBacklight {int(value)}', expect_response=False)

    def options(self, fg: int, bg: int, transparent: int) -> None:
        """Sets the options for the LCD.
        Args:
            fg (int): The foreground color.
            bg (int): The background color.
            transparent (int): The transparency (1 for on, 0 for off).
        """
        self.conn.execute(f'LCDOptions {int(fg)} {int(bg)} {int(transparent)}', expect_response=False)

    def verbose(self, value: int) -> None:
        """Sets the verbosity of the LCD.
        Args:
            value (int): The verbosity level (1 for on, 0 for off).
        """
        self.conn.execute(f'LCDVerbose {int(value)}', expect_response=False)
