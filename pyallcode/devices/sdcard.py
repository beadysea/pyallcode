"""Module for interacting with the SD card device."""
from ..comm.connection import Connection
from .base import DeviceBase

class SDCard(DeviceBase):
    """Represents the SD card interface on the robot.
    
     Args:
        conn (Connection): The connection object for sending commands.

        Attributes:
            conn (Connection): The connection object for sending commands.
    """
    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initialize the SDCard interface with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def init(self) -> int:
        """Initialize the SD card."""
        return int(self.conn.execute('CardInit', True, 2) or -1)

    def create(self, filename: str) -> int:
        """Create a new file on the SD card.
        
        Args:
            filename (str): The name of the file to create.

            Returns:
                int: The result of the create operation.
        """
        return int(self.conn.execute(f'CardCreate {filename}', True, 2) or -1)

    def open(self, filename: str) -> int:
        """Open a file on the SD card.

        Args:
            filename (str): The name of the file to open.

        Returns:
            int: The result of the open operation.
        """
        return int(self.conn.execute(f'CardOpen {filename}', True, 2) or -1)

    def delete(self, filename: str) -> int:
        """Delete a file on the SD card.

        Args:
            filename (str): The name of the file to delete.

        Returns:
            int: The result of the delete operation.
        """
        return int(self.conn.execute(f'CardDelete {filename}', True, 2) or -1)

    def write_byte(self, data: int) -> None:
        """Write a byte to the SD card.
        Args:
            data (int): The byte value to write (0-255).

        Raises:
            ValueError: If the data is not an integer or is out of range.
        
        """
        if not isinstance(data, int) or not (0 <= data <= 255):
            raise ValueError("write_byte expects 0..255")
        self.conn.execute(f'CardWriteByte {data}', expect_response=False)

    def read_byte(self) -> int:
        """Read a byte from the SD card.
        
        Returns:
            int: The byte value read (0-255).
        """
        return int(self.conn.execute('CardReadByte', True, 2) or -1)

    def record_mic(self, bitdepth: int, samplerate: int, seconds: int, filename: str, timeout: int | None = None) -> int:
        """Record audio from the microphone to a file on the SD card.

        Args:
            bitdepth (int): The bit depth of the audio (e.g., 16).
            samplerate (int): The sample rate of the audio (e.g., 44100).
            seconds (int): The duration to record in seconds.
            filename (str): The name of the file to save the recording.
            timeout (int | None): The timeout for the operation in seconds.

        Returns:
            int: The result of the record operation.
        """
        effective_timeout = seconds + 5 if timeout is None else timeout
        return int(self.conn.execute(f'CardRecordMic {int(bitdepth)} {int(samplerate)} {int(seconds)} {filename}', True, effective_timeout) or -1)

    def playback(self, filename: str, timeout: int = 50) -> int:
        """Play back an audio file from the SD card.
        Args:
            filename (str): The name of the file to play back.
            timeout (int): The timeout for the operation in seconds.

        Returns:
            int: The result of the playback operation.
        """
        return int(self.conn.execute(f'CardPlayback {filename}', True, timeout) or -1)

    def bitmap(self, x: int, y: int, filename: str) -> int:
        """Display a bitmap image on the LCD screen.
    
        Args:
            x (int): The x-coordinate to display the image.
            y (int): The y-coordinate to display the image.
            filename (str): The name of the bitmap file to display.

        Returns:
            int: The result of the bitmap operation.
        """
        safe_filename = '"' + str(filename).replace('"', '') + '"'
        return int(self.conn.execute(f'CardBitmap {int(x)} {int(y)} {safe_filename}', True, 5) or -1)
