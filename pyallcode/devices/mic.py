from pyallcode.serial_comms import CommunicationDevice


class Mic:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read_level(self) -> int:
        """Reads the value of the microphone

        Returns:
            int: the value of the microphone.
        """
        return self.device.send_message("ReadMic\n")
