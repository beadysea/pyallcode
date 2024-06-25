# Module allcode.devices.leds

## class LEDS

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
