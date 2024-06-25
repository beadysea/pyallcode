# Module allcode.devices.lcd

## class LCD

Methods:

### clear() -> int

Clears the LCD screen.

### display_text(self, x: int, y: int, text: str) -> None

Displays the given text on the LCD screen at the given x and y coordinates.

Args:
>x (int): x co-ordinate between 0 and 127
>
>y (int): y co-ordinate between 0 and 31
>
>text (str): text to display on the LCD.

Raises:
>ValueError: when the x or y co-ordinates are out of range.

### display_int(self, x: int, y: int, value: int) -> None

Displays the given value on the LCD screen at the given x and y coordinates.

Args:
>x (int): x co-ordinate between 0 and 127
>
>y (int): y co-ordinate between 0 and 31
>
>value (int): value to display on the LCD.

Raises:
>ValueError: when the x or y co-ordinate is out of range.

### plot_pixel(self, x: int, y: int)

Plots a pixel on the LCD screen at the given x and y coordinates.

Args:
>x (int): x co-ordinate between 0 and 127
>
>y (int): y co-ordinate between 0 and 31

Raises:
>ValueError: when the x or y co-ordinate is out of range.

### clear_pixel(self, x: int, y: int)

Clears a pixel on the LCD screen at the given x and y coordinates.

Args:
>x (int): x co-ordinate between 0 and 127
>
>y (int): y co-ordinate between 0 and 31

Raises:
>ValueError: when the x or y co-ordinate is out of range.

### draw_line(self, x1: int, y1: int, x2: int, y2: int) -> None

Draws a line on the LCD screen between two points (x1,y1) and (x2,y2).

Args:
>x1 (int): x co-ordinate of the first point between 0 and 127
>
>y1 (int): y co-ordinate of the first point between 0 and 31
>
>x2 (int): x co-ordinate of the second point between 0 and 127
>
>y2 (int): y co-ordinate of the second point between 0 and 31

Raises:
>ValueError: when any x or y co-ordinate is out of range.

### draw_rectangle(self, x1: int, y1: int, x2: int, y2: int) -> None

Draws a rectangle on the LCD screen between two points (x1,y1) and (x2,y2).

Args:
>x1 (int): x co-ordinate of the first point between 0 and 127
>
>y1 (int): y co-ordinate of the first point between 0 and 31
>
>x2 (int): x co-ordinate of the second point between 0 and 127
>
>y2 (int): y co-ordinate of the second point between 0 and 31

Raises:
>ValueError: when any x or y co-ordinate is out of range.

### display_bitmap(self, x: int, y: int, filename: str) -> int

Displays a bitmap on the LCD screen at the given x and y coordinates.

Args:
>x (int): x co-ordinate between 0 and 127
>
>y (int): y co-ordinate between 0 and 31
filename (str): a bitmap file.

Returns:
>int:

### backlight_brightness(self, brightness: int) -> None

Sets the brightness of the LCD backlight.

Args:
>brightness (int): brightness value between 0 and 100

Raises:
>ValueError: when the brightness is out of range.

### options(self, foreground: Colour, background: Colour, transparent: bool) -> None

Sets the foreground and background colour of the LCD screen.

Args:
>foreground (Colour): Enum of the foreground colour
>
>background (Colour): Enum of the background colour
>
>transparent (bool): Transparency of the LCD screen
