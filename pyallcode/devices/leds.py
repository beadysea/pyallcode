from pyallcode.serial_comms import CommunicationDevice

MIN_LED = 0
MIN_LED_VALUE = 0
MAX_LED = 7
MAX_LED_VALUE = 255


class LEDs:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def write(self, value: int):
        """Writes the given value to the LEDs

        Args:
            value (int): Value to write to the LEDs between 0 and 255

        Raises:
            ValueError: when value is out of range.
        """
        if value not in range(MIN_LED_VALUE, MAX_LED_VALUE + 1):
            raise ValueError(
                "Invalid value {value}. The value must be in the range {MIN_LED_VALUE} to {MAX_LED_VALUE}.".format(
                    value=value,
                    MIN_LED_VALUE=MIN_LED_VALUE,
                    MAX_LED_VALUE=MAX_LED_VALUE,
                )
            )
        self.device.send_message(f"LEDWrite {value}")

    def on(self, led: int):
        """Switches the given LED on.

        Args:
            led (int): The LED number between 0 and 7

        Raises:
            ValueError: when the LED number is out of range.
        """
        if led not in range(MIN_LED, MAX_LED + 1):
            raise ValueError(
                "Invalid led value {led}. Led value must be in the range {MIN_LED} to {MAX_LED}.".format(
                    led=led,
                    MIN_LED=MIN_LED,
                    MAX_LED=MAX_LED,
                )
            )
        self.device.send_message(f"LEDOn {led}")

    def off(self, led: int):
        """Switches the given LED off.

        Args:
            led (int): The LED number between 0 and 7

        Raises:
            ValueError: when the LED number is out of range.
        """
        if led not in range(MIN_LED, MAX_LED + 1):
            raise ValueError(
                "Invalid led value {led}. Led value must be in the range {MIN_LED} to {MAX_LED}.".format(
                    led=led,
                    MIN_LED=MIN_LED,
                    MAX_LED=MAX_LED,
                )
            )
        self.device.send_message(f"LEDOff {led}")
