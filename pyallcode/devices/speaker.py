from allcode.serial_comms import CommunicationDevice

MIN_NOTE_DURATION = 1
MAX_NOTE_DURATION = 10001
MIN_FREQUENCY = 1
MAX_FREQUENCY = 10001

class Speaker:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def play_note(self, frequency: int, duration: int):
        """Plays a note at the given frequency for the given time.

        Args:
            frequency (int): frequency of the note between 1 and 10000 Hz.
            time (int): duration of the note between 1 and 10000 milliseconds

        Raises:
            ValueError: when the frequency or duration is out of range.
        """
        if not frequency in range(MIN_FREQUENCY, MAX_FREQUENCY):
            raise ValueError(
                f'Invalid fequency {frequency}Hz. The frequency must be in the range {MIN_FREQUENCY} to {MAX_FREQUENCY-1} Hertz.')
        if not duration in range(MIN_NOTE_DURATION, MAX_NOTE_DURATION):
            raise ValueError(
                f'Invalid note duration {duration}ms. Note duration must be in the range {MIN_NOTE_DURATION} to {MAX_NOTE_DURATION-1} milliseconds.')
        command = f'PlayNote {frequency} {duration}\n'
        self.device.send_message(command)
