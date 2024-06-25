from allcode.enums import BitDepth, SampleRate
from allcode.serial_comms import CommunicationDevice


MIN_SD_BYTE = 0
MAX_SD_BYTE = 255
MIN_RECORD_TIME = 0
MAX_RECORD_TIME = 65535


class SDCard:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def init(self) -> int:
        """Initialises the SD Card.

        Returns:
            int: Status 0 (OK), 254 (error) or 255 (no card)
        """
        command = 'CardInit\n'
        return self.device.send_message(command)

    def create_file(self, filename: str) -> int:
        """Creates a file on the SD Card.

        Args:
            filename (str): the filename of the file to be created.

        Returns:
            int: Status 0 (OK), 1 (file exists) or 255 (error)

        """
        command = f'CardCreate {filename}\n'
        return self.device.send_message(command)

    def open_file(self, filename: str) -> int:
        """Opens a file stored on the SD Card

        Args:
            filename (str): the name of the file to open.

        Returns:
            int: Status 0 (OK), 239 (file not found) or 255 (error)
        """
        command = f'CardOpen {filename}\n'
        return self.device.send_message(command)

    def delete_file(self, filename: str) -> int:
        """Deletes a file from the SD CArd

        Args:
            filename (str): the name of the file to delete.

        Returns:
            int: Status 0 (OK) or 255 (error)
        """
        command = f'CardDelete {filename}\n'
        return self.device.send_message(command)

    def write_byte(self, data: int) -> int:
        """Writes the given byte to the currently open SD Card file.

        Args:
            data (int): the byte to write to the file.

        Raises:
            ValueError: when the data byte value is out of range.

        Returns:
            int: Status = 0 (OK) or 255 (error)
        """
        if data < MIN_SD_BYTE or data > MAX_SD_BYTE:
            raise ValueError(
                f'Invalid data {data}. data value must be in the range {MIN_SD_BYTE} to {MAX_SD_BYTE}.')
        command = f'CardWriteByte {data}\n'
        return self.device.send_message(command)

    def read_byte(self) -> int:
        """Reads a byte from the currently open SD Card file.

        Returns:
            int: the value of the data byte.
        """
        command = f'CardReadByte\n'
        return self.device.send_message(command)

    def record_mic(self, bitdepth: BitDepth, samplerate: SampleRate, time: int, filename: str) -> int:
        """Records digital audio from the microphone to the given SD Card file.

        Args:
            bitdepth (BitDepth): Enum of the bit depth
            samplerate (SampleRate): Enum of the sample rate
            time (int): tine to record between 0 and 65535 seconds.
            filename (str): the name of the wav file stored on the SD Card

        Raises:
            ValueError: when the time is out of range.

        Returns:
            int: Status 0 (OK), 239 (file exists) or 255 (error)
        """
        if time < MIN_RECORD_TIME or time > MAX_RECORD_TIME:
            raise ValueError(
                f'Invalid time: {time} seconds. time must be in the range {MIN_RECORD_TIME} to {MAX_RECORD_TIME} seconds.')
        command = f'CardRecordMic {bitdepth} {samplerate} {time} {filename}\n'
        return self.device.send_message(command)

    def playback(self, filename: str) -> int:
        """Plays the given SD Card wav file.

        Args:
            filename (str): the name of the wav file.

        Returns:
            int: Status 0 (OK), 239 (file not found) or 255 (error)
        """
        command = f'CardPlayBack {filename}\n'
        return self.device.send_message(command)
