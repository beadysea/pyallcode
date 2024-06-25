from allcode.serial_comms import CommunicationDevice


class Mic:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read(self) -> int:
        """Reads the value of the microphone

        Returns:
            int: the value of the microphone.
        """
        command = 'ReadMic\n'
        return self.device.send_message(command)