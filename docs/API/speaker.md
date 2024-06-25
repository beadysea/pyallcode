# Module allcode.devices.speaker

## class Speaker

### play_note(self, frequency: int, duration: int)

Plays a note at the given frequency for the given time.

Args:
>frequency (int): frequency of the note between 1 and 10000 Hz.
>
>duration of the note between 1 and 10000 milliseconds

Raises:
>ValueError: when the frequency or duration is out of range.
