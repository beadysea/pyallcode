from pyallcode.serial_comms import CommunicationDevice


class LightSensor:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read(self) -> int:
        """Reads the value of the light sensor.

        Returns:
            int: the value of the light sensor.
        """
        return self.device.send_message("ReadLight\n")
