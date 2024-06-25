"""Simulated Formula AllCode Device Connection.

File: protocol_simfad.py
Author: Bill Crawford <bill.crawford@forthvalley.ac.uk>

This module implements a simulated connection to a formula allcode device.
The pyAllcode API sends data to the serial port. The data is then read by
this module and processed as if it was coming from a real device.

The purpose of this module is to test the functionality of control software
writtten by the developer using the pyAllcode API.

This file is part of the pyAllcode API for the Formula AllCode robot.
(c) 2023-2024 Bill Crawford <bill.crawford@forthvalley.ac.uk>

URL format:   simfad://[option[/option...]]
options:
- logging={debug|info|warning|error}  - enable logging at the given level
"""

import logging
import urllib.parse as urlparse
import queue

from serial.serialutil import SerialBase
from serial.serialutil import SerialException
from serial.serialutil import PortNotOpenError

# map log level names to constants. used in fromURL()
LOGGER_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "not set": logging.NOTSET,
}


class Serial(SerialBase):
    """Serial port implementation that simulates a connection in software."""

    BAUDRATES = (
        50,
        75,
        110,
        134,
        150,
        200,
        300,
        600,
        1200,
        1800,
        2400,
        4800,
        9600,
        19200,
        38400,
        57600,
        115200,
    )

    def __init__(self, *args, **kwargs):
        """Initialize the Serial port with the given settings."""
        # set up default values
        self.input_buffer_size = 4096
        self.output_buffer_size = 4096
        # self.queue = None
        self.logger = None
        self._cancel_write = False
        super(Serial, self).__init__(*args, **kwargs)

    def open(self):
        """Open port with current settings.
        This may throw a SerialException if the port cannot be opened.
        """
        if self.is_open:
            raise SerialException("Port is already open.")
        self.logger = None
        self.input_buffer = queue.Queue(self.input_buffer_size)
        self.output_buffer = queue.Queue(self.output_buffer_size)

        if self._port is None:  # type: ignore inherited from SerialBase.
            raise SerialException("Port must be configured before it can be opened.")

        self.from_URL(self.port)
        self._isOpen = True
        self.flush_input_buffer()
        self.flush_output_buffer()

    def flush_input_buffer(self):
        """Clear input buffer
        discards everything in the buffer."""
        if not self.is_open:
            raise PortNotOpenError()
        if self.logger:
            self.logger.info("reset_input_buffer()")
        try:
            while self.input_buffer.qsize():
                self.input_buffer.get_nowait()
        except queue.Empty:
            pass

    def flush_output_buffer(self):
        """Clear output buffer
        aborts the current output and discards everything in the buffer.
        """
        if not self.is_open:
            raise PortNotOpenError()
        if self.logger:
            self.logger.info("reset_output_buffer()")
        try:
            while self.output_buffer.qsize():
                self.output_buffer.get_nowait()
        except queue.Empty:
            pass

    def close(self):
        """Close port"""
        if self._isOpen:
            self._isOpen = False
            try:
                self.input_buffer.get_nowait()
            except queue.Empty:
                pass
            try:
                self.output_buffer.put_nowait(None)
            except queue.Full:
                pass
        super(Serial, self).close()

    def from_URL(self, url):
        """extract host and port from an URL string"""
        parts = urlparse.urlsplit(url)
        if parts.scheme != "simfad":
            raise SerialException(
                "expected a string in the form "
                "'simfad://[?logging=(debug|info|warning|error)]'"
                ": not starting with simfad:// {}".format(parts.scheme)
            )
        try:
            # is there a "path" (our options)?
            if "/" in url:
                for option, values in urlparse.parse_qs(parts.query, True).items():
                    if option == "logging":
                        logging.basicConfig()  # XXX is it good to call here?
                        self.logger = logging.getLogger("pyAllcode.simfad")
                        self.logger.setLevel(LOGGER_LEVELS[values[0]])
                        self.logger.debug("enabled logging: {}".format(values[0]))
                    else:
                        raise ValueError("unknown option: {}".format(option))

        except ValueError as e:
            raise SerialException(
                "expected a string in the form"
                '"simfad://[?logging=(debug|info|warning|error)]"'
                ": {}".format(e)
            )

    def read(self, size=1):
        """Read size bytes from the serial port.
        If a timeout is set it may return less characters as requested.
        """
        if not self.is_open:
            raise PortNotOpenError()
        if self.logger:
            self.logger.debug("read({})".format(size))
        if size < 0:
            raise ValueError("size must be >= 0")
        if size == 0:
            return b""
        data = bytearray()
        try:
            for _ in range(size):
                data.append(self.input_buffer.get(timeout=self.timeout))
        except queue.Empty:
            pass
        return bytes(data)

    def write(self, data):
        """Output the given byte string over the serial port."""
        if not self.is_open:
            raise PortNotOpenError()
        if self.logger:
            self.logger.debug("write({})".format(data))
        for byte in data:
            self.output_buffer.put(byte)
        return len(data)

    # - - - platform specific - - -
    # None so far


# simple client test
if __name__ == "__main__":
    import sys

    s = Serial("simfad://")
    sys.stdout.write("{}\n".format(s))

    sys.stdout.write("write...\n")
    s.write("hello\n".encode())
    s.flush()
    sys.stdout.write("read: {}\n".format(s.read(5)))

    s.close()
