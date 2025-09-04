from pyallcode.enums import Axis
from pyallcode.serial_comms import CommunicationDevice


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
        return self.device.send_message(f"ReadAxis {axis.value}\n")
