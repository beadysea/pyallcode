# Module allcode.devices.sd_card

## class SDCard

### init(self) -> int

Initialises the SD Card.

Returns:
>int: Status 0 (OK), 254 (error) or 255 (no card)

### create_file(self, filename: str) -> int

Creates a file on the SD Card.

Args:
>filename (str): the filename of the file to be created.

Returns:
>int: Status 0 (OK), 1 (file exists) or 255 (error)

### open_file(self, filename: str) -> int

Opens a file stored on the SD Card

Args:
>filename (str): the name of the file to open.

Returns:
>int: Status 0 (OK), 239 (file not found) or 255 (error)

### delete_file(self, filename: str) -> int

Deletes a file from the SD CArd

Args:
>filename (str): the name of the file to delete.

Returns:
>int: Status 0 (OK) or 255 (error)

### write_byte(self, data: int) -> int

Writes the given byte to the currently open SD Card file.

Args:
>data (int): the byte to write to the file.

Raises:
>ValueError: when the data byte value is out of range.

Returns:
>int: Status = 0 (OK) or 255 (error)

### read_byte(self) -> int

Reads a byte from the currently open SD Card file.

Returns:
>int: the value of the data byte.

### record_mic(self, bitdepth: BitDepth, samplerate: SampleRate, time: int, filename: str) -> int

Records digital audio from the microphone to the given SD Card file.

Args:
>bitdepth (BitDepth): Enum of the bit depth
>
>samplerate (SampleRate): Enum of the sample rate
>
>time (int): tine to record between 0 and 65535 seconds.
>
>filename (str): the name of the wav file stored on the SD Card

Raises:
>ValueError: when the time is out of range.

Returns:
>int: Status 0 (OK), 239 (file exists) or 255 (error)

### playback(self, filename: str) -> int

Plays the given SD Card wav file.

Args:
>filename (str): the name of the wav file.

Returns:
>int: Status 0 (OK), 239 (file not found) or 255 (error)
