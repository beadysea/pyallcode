from allcode.serial_comms import CommunicationDevice

MIN_LED = 0 
MIN_LED_VALUE = 0
MAX_LED = 8
MAX_LED_VALUE = 256


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
        if value not in range(MIN_LED_VALUE,MAX_LED_VALUE):
            raise ValueError(
                f'Invalid value {value}. The value must be in the range {MIN_LED_VALUE} to {MAX_LED_VALUE-1}.')
        command = f'LEDWrite {value}'
        self.device.send_message(command)

    def on(self, led: int):
        """Switches the given LED on.

        Args:
            led (int): The LED number between 0 and 7

        Raises:
            ValueError: when the LED number is out of range. 
        """
        if led not in range(MIN_LED, MAX_LED):
            raise ValueError(
                f'Invalid led value {led}. Led value must be in the range {MIN_LED} to {MAX_LED-1}.')
        command = f'LEDOn {led}'
        self.device.send_message(command)

    def off(self, led: int):
        """Switches the given LED off.

        Args:
            led (int): The LED number between 0 and 7 

        Raises:
            ValueError: when the LED number is out of range.
        """
        if led not in range(MIN_LED,MAX_LED):
            raise ValueError(
                f'Invalid led value {led}. Led value must be in the range {MIN_LED} to {MAX_LED-1}.')
        command = f'LEDOff {led}'
        self.device.send_message(command)