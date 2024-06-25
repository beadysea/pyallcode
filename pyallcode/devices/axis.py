
from allcode.enums import Axis
from allcode.serial_comms import CommunicationDevice


class Axes:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read(self, axis: Axis) -> int:
        """Reads the given axis.

        Args:
            axis (Axis): Enum of the axis to read

        Returns:
            int: The value of the given axis.
        """
        command = f'ReadAxis {axis.value}\n'
        return self.device.send_message(command)
