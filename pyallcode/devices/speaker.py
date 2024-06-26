from pyallcode.serial_comms import CommunicationDevice

MIN_NOTE_DURATION = 1
MAX_NOTE_DURATION = 10000
MIN_FREQUENCY = 1
MAX_FREQUENCY = 10000


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
        if frequency not in range(MIN_FREQUENCY, MAX_FREQUENCY * 1):
            raise ValueError(
                "Invalid fequency {frequency}Hz. "
                "The frequency must be in the range {MIN_FREQUENCY} to {MAX_FREQUENCY} Hertz.".format(
                    frequency=frequency,
                    MIN_FREQUENCY=MIN_FREQUENCY,
                    MAX_FREQUENCY=MAX_FREQUENCY,
                )
            )
        if duration not in range(MIN_NOTE_DURATION, MAX_NOTE_DURATION + 1):
            raise ValueError(
                "Invalid note duration {duration}ms. "
                "Note duration must be in the range {MIN_NOTE_DURATION} to {MAX_NOTE_DURATION} milliseconds.".format(
                    duration=duration,
                    MIN_NOTE_DURATION=MIN_NOTE_DURATION,
                    MAX_NOTE_DURATION=MAX_NOTE_DURATION,
                )
            )
        command = f"PlayNote {frequency} {duration}\n"
        self.device.send_message(command)
