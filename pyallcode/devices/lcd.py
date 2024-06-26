from pyallcode.enums import Colour
from pyallcode.serial_comms import CommunicationDevice

MIN_LCD_X = 0
MAX_LCD_X = 127
MIN_LCD_Y = 0
MAX_LCD_Y = 31
MIN_LCD_BRIGHTNESS = 0
MAX_LCD_BRIGHTNESS = 100


class LCD:

    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def clear(self):
        """Clears the LCD screen."""
        command = "LCDClear\n"
        self.device.send_message(command)

    def display_text(self, x: int, y: int, text: str):
        """Displays the given text on the LCD screen at the given x and y coordinates.

        Args:
            x (int): x co-ordinate between 0 and 127
            y (int): y co-ordinate between 0 and 31
            text (str): text to display on the LCD.

        Raises:
            ValueError: when the x or y co-ordinates are out of range.
        """
        if x not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x value {x}. x value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x=x, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y not in range(MIN_LCD_Y, MAX_LCD_Y + 1):
            raise ValueError(
                "Invalid y value {y}. y value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y=y, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )

        command = f"LCDPrint {x} {y} {text}\n"
        self.device.send_message(command)

    def display_int(self, x: int, y: int, value: int):
        """Displays the given value on the LCD screen at the given x and y coordinates.

        Args:
            x (int): x co-ordinate between 0 and 127
            y (int): y co-ordinate between 0 and 31
            value (int): value to display on the LCD.

        Raises:
            ValueError: when the x or y co-ordinate is out of range.
        """
        if x not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x value {x}. x value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x=x, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y not in range(MIN_LCD_Y, MAX_LCD_Y + 1):
            raise ValueError(
                "Invalid y value {y}. y value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y=y, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )

        command = f"LCDNumber {x} {y} {value}\n"
        self.device.send_message(command)

    def plot_pixel(self, x: int, y: int):
        """Plots a pixel on the LCD screen at the given x and y coordinates.

        Args:
            x (int): x co-ordinate between 0 and 127
            y (int): y co-ordinate between 0 and 31

        Raises:
            ValueError: when the x or y co-ordinate is out of range.
        """
        if x not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x value {x}. x value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x=x, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y not in range(MIN_LCD_Y, MAX_LCD_Y + 1):
            raise ValueError(
                "Invalid y value {y}. y value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y=y, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )

        command = f"LCDPixel {x} {y} 1\n"
        self.device.send_message(command)

    def clear_pixel(self, x: int, y: int):
        """Clears a pixel on the LCD screen at the given x and y coordinates.

        Args:
            x (int): x co-ordinate between 0 and 127
            y (int): y co-ordinate between 0 and 31

        Raises:
            ValueError: when the x or y co-ordinate is out of range.
        """
        if x not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x value {x}. x value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x=x, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y < MIN_LCD_Y or y > MAX_LCD_Y:
            raise ValueError(
                "Invalid y value {y}. y value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y=y, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )

        command = f"LCDPixel {x} {y} 0\n"
        self.device.send_message(command)

    def draw_line(self, x1: int, y1: int, x2: int, y2: int):
        """Draws a line on the LCD screen between two points (x1,y1) and (x2,y2).

        Args:
            x1 (int): x co-ordinate of the first point between 0 and 127
            y1 (int): y co-ordinate of the first point between 0 and 31
            x2 (int): x co-ordinate of the second point between 0 and 127
            y2 (int): y co-ordinate of the second point between 0 and 31

        Raises:
            ValueError: when any x or y co-ordinate is out of range.
        """
        if x1 not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x1 value {x1}. x1 value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x1=x1, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y1 not in range(MIN_LCD_Y, MAX_LCD_Y + 1):
            raise ValueError(
                "Invalid y1 value {y1}. y1 value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y1=y1, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )
        if x2 not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x2 value {x2}. x2 value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x2=x2, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y2 not in range(MIN_LCD_Y, MAX_LCD_Y + 1):
            raise ValueError(
                "Invalid y2 value {y2}. y2 value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y2=y2, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )
        command = f"LCDLine {x1} {y1} {x2} {y2}\n"
        self.device.send_message(command)

    def draw_rectangle(self, x1: int, y1: int, x2: int, y2: int):
        """Draws a rectangle on the LCD screen between two points (x1,y1) and (x2,y2).

        Args:
            x1 (int): x co-ordinate of the first point between 0 and 127
            y1 (int): y co-ordinate of the first point between 0 and 31
            x2 (int): x co-ordinate of the second point between 0 and 127
            y2 (int): y co-ordinate of the second point between 0 and 31

        Raises:
            ValueError: when any x or y co-ordinate is out of range.
        """
        if x1 not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x1 value {x1}. x1 value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x1=x1, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y1 not in range(MIN_LCD_Y, MAX_LCD_Y + 1):
            raise ValueError(
                "Invalid y1 value {y1}. y1 value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y1=y1, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )
        if x2 not in range(MIN_LCD_X, MAX_LCD_X + 1):
            raise ValueError(
                "Invalid x2 value {x2}. x2 value must be in the range {MIN_LCD_X} to {MAX_LCD_X}.".format(
                    x2=x2, MIN_LCD_X=MIN_LCD_X, MAX_LCD_X=MAX_LCD_X
                )
            )
        if y2 not in range(MIN_LCD_Y, MAX_LCD_Y + 1):
            raise ValueError(
                "Invalid y2 value {y2}. y2 value must be in the range {MIN_LCD_Y} to {MAX_LCD_Y}.".format(
                    y2=y2, MIN_LCD_Y=MIN_LCD_Y, MAX_LCD_Y=MAX_LCD_Y
                )
            )
        command = f"LCDRect {x1} {y1} {x2} {y2}\n"
        self.device.send_message(command)

    def display_bitmap(self, x: int, y: int, filename: str) -> int:
        """Displays a bitmap on the LCD screen at the given x and y coordinates.

        Args:
            x (int): x co-ordinate between 0 and 127
            y (int): y co-ordinate between 0 and 31
            filename (str): a bitmap file.

        Returns:
            int:
        """
        command = f"CardBitmap {x} {y} {filename}\n"
        return self.device.send_message(command)

    def backlight_brightness(self, brightness: int):
        """Sets the brightness of the LCD backlight.

        Args:
            brightness (int): brightness value between 0 and 100

        Raises:
            ValueError: when the brightness is out of range.
        """
        if brightness not in range(MIN_LCD_BRIGHTNESS, MAX_LCD_BRIGHTNESS + 1):
            raise ValueError(
                "Invalid brightness value {brightness}. "
                "Brightness must be in the range {MIN_LCD_BRIGHTNESS} to {MAX_LCD_BRIGHTNESS}.".format(
                    brightness=brightness,
                    MIN_LCD_BRIGHTNESS=MIN_LCD_BRIGHTNESS,
                    MAX_LCD_BRIGHTNESS=MAX_LCD_BRIGHTNESS,
                )
            )

        command = f"LCDBacklight {brightness}\n"
        self.device.send_message(command)

    def options(self, foreground: Colour, background: Colour, transparent: bool):
        """Sets the foreground and background colour of the LCD screen.

        Args:
            foreground (Colour): Enum of the foreground colour
            background (Colour): Enum of the background colour
            transparent (bool): Transparency of the LCD screen
        """
        if transparent:
            command = f"LCDOptions {foreground.value} {background.value} 1\n"
        else:
            command = f"LCDOptions {foreground.value} {background.value} 0\n"
        self.device.send_message(command)
