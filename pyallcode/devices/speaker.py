""""Speaker device module."""
import time
from ..comm.connection import Connection
from .base import DeviceBase

class Speaker(DeviceBase):
    """Represents the speaker device.
    Args:
        conn (Connection): The connection to the device.
    """

    def __init__(self, conn: Connection | None = None, port: str | int | None = None, autoconn: bool = True, verbose: int = 0) -> None:
        """Initializes the Speaker with an existing or self-managed connection."""
        super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)

    def play_note(self, note: int, length_ms: int) -> None:
        """Plays a note on the speaker.
        Args:
            note (int): The note to play.
            length_ms (int): The duration of the note in milliseconds.
        """
        self.conn.execute(f'PlayNote {int(note)} {int(length_ms)}', expect_response=False)
        time.sleep(max(0, length_ms) / 1000.0)
