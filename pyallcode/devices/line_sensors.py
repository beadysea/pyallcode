from allcode.enums import LineSensor
from allcode.serial_comms import CommunicationDevice


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
        command = f'ReadLine {line_sensor.value}\n'
        return self.device.send_message(command)