from pyallcode.enums import LineSensor
from pyallcode.serial_comms import CommunicationDevice


class LineSensors:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read(self, line_sensor: LineSensor) -> int:
        """Reads the value of the given line sensor.

        Args:
            line_sensor (LineSensor): Enum of the line sensor.

        Returns:
            int: the value of the line sensor.
        """
        return self.device.send_message(f"ReadLine {line_sensor.value}\n")
