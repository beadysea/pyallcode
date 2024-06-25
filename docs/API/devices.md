# Package allcode.devices

The allcode API v2.0.0 seperates out the buggy peripheral devices in this sub-package. This gives the added benefit that the peripherals can be used individually or as part of the buggy.

```python
# Example using peripherals as part of the buggy.
from allcode.buggy import Buggy
from allcode.enums import LineSensor
from allcode.serial_comms import SerialDevice

car = Buggy(SerialDevice())
car.leds.write(248)
left_line = car.line_sensors.read(LineSensor.LEFT)
```

```python
# Example using peripherals individually.
from allcode.devices.leds import LEDS
from allcode.devices.line_sensors import LineSensors
from allcode.enums import LineSensor
from allcode.serial_comms import SerialDevice

serial = SerialDevice()
leds = LEDS(serial)
line_sensors = LineSensors(serial)

leds.write(248)
left_line = line_sensors.read(LineSensor.LEFT)
print(left_line)
``` 

The allcode devices sub-package contains all the methods for the peripherals connected to the formula allcode buggy.

## class axes.Axes

Methods:

### read(axis: Axis) -> int

Reads the given axis.

Args:
> axis (Axis): Enum of the axis to read

Returns:
> int: The value of the given axis.

## class buttons.Buttons

Methods:

### read(buttons: Button) -> bool

Reads the state of the given button.

Args:
> button (Button): Enum of the button.

Returns:
>bool: State of the given button.

## class ir_sensors.IRSensors

Methods:

### read(sensor: int) -> int

Reads the value of the given sensor.

Args:
>sensor (int): Number of sensor to read between 0 and 7

Raises:
>ValueError: when the sensor number is out of range.

Returns:
>int: the value of the given sensor.

## class lcd.LCD

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

### plot_pixel(self, x: int, y: int):

Plots a pixel on the LCD screen at the given x and y coordinates.

Args:
>x (int): x co-ordinate between 0 and 127
>
>y (int): y co-ordinate between 0 and 31

Raises:
>ValueError: when the x or y co-ordinate is out of range.

### clear_pixel(self, x: int, y: int):

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

## class leds.LEDS

### write(self, value: int)

Writes the given value to the LEDs

Args:
>value (int): Value to write to the LEDs between 0 and 255

Raises:
>ValueError: when value is out of range.

### on(self, led: int)

Switches the given LED on.

Args:
>led (int): The LED number between 0 and 7

Raises:
>ValueError: when the LED number is out of range.

### off(self, led: int)

Switches the given LED off.

Args:
>led (int): The LED number between 0 and 7 

Raises:
>ValueError: when the LED number is out of range.

## class light_sensor.LightSensor

### read(self) -> int

Reads the value of the light sensor.

Returns:
>int: the value of the light sensor.

## class line_sensors.LineSensors

### read(self, line_sensor: LineSensor) -> int

Reads the value of the given line sensor.

Args:
>line_sensor (LineSensor): Enum of the line sensor.

Returns:
>int: the value of the line sensor.

## class mic.Mic

### read(self) -> int

Reads the value of the microphone

Returns:
>int: the value of the microphone.

## class sd_card.SDCard

### init(self) -> int

Initialises the SD Card.

Returns:
>int: Status 0 (OK), 254 (error) or 255 (no card)

### create_file(self, filename: str) -> int:

Creates a file on the SD Card.

Args:
>filename (str): the filename of the file to be created.

Returns:
>int: Status 0 (OK), 1 (file exists) or 255 (error)

### open_file(self, filename: str) -> int

Opens a file stored on the SD Card

Args:
>filename (str): the name of the file to open.

Returns:
>int: Status 0 (OK), 239 (file not found) or 255 (error)

### delete_file(self, filename: str) -> int:

Deletes a file from the SD CArd

Args:
>filename (str): the name of the file to delete.

Returns:
>int: Status 0 (OK) or 255 (error)

### write_byte(self, data: int) -> int

Writes the given byte to the currently open SD Card file.

Args:
>data (int): the byte to write to the file.

Raises:
>ValueError: when the data byte value is out of range.

Returns:
>int: Status = 0 (OK) or 255 (error)
