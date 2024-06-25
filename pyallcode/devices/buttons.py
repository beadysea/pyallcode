
from allcode.enums import Button
from allcode.serial_comms import CommunicationDevice


class Buttons:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read(self, button: Button) -> bool:
        """Reads the state of the given button.

        Args:
            button (Button): Enum of the button.

        Returns:
            bool: State of the given button
        """
        command = f'ReadSwitch {button.value}\n'
        value = self.device.send_message(command)
        if value == 1:
            return True
        else:
            return False