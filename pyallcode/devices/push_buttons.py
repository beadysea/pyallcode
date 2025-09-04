from pyallcode.enums import Button
from pyallcode.serial_comms import CommunicationDevice


class PushButtons:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read(self, button: Button) -> bool:
        """Reads the state of the given button.

        Args:
            button (Button): Enum of the button.

        Returns:
            bool: State of the given button
        """
        value = self.device.send_message(f"ReadSwitch {button.value}\n")
        if value == 1:
            return True
        else:
            return False
