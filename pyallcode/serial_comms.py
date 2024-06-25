from abc import ABC
import serial
import serial.serialutil


class CommunicationDevice(ABC):
    """Communications Protocol"""

    # Implements a context manager
    def __enter__(self): ...

    def __exit__(self, *args): ...
    def _flush(self): ...

    def send_message(self, data: str) -> int: ...


class SerialDevice(CommunicationDevice):
    """Serial Device implementation of communication interface"""

    def __init__(self, baudrate: int = 115200, timeout: int = 1) -> None:
        try:
            self.serial = serial.serial_for_url(
                url="hwgrep://", baudrate=baudrate, timeout=timeout
            )
            self.serial.close()
        except serial.SerialException:
            try:
                self.serial = serial.serial_for_url(
                    url="simfad://", baudrate=baudrate, timeout=timeout
                )
                self.serial.close()
            except serial.SerialException:
                raise serial.SerialException("No serial device found")

    def _flush(self):
        count = self.serial.in_waiting
        while count > 0:
            self.serial.readline().rstrip()
            count = self.serial.in_waiting

    # Methods implementing a communication interface
    def send_message(self, message: str) -> int | None:
        """Sends a message to the serial device.
        Return: the response or status.
        """
        with self.serial:
            # self._flush()
            status = self.serial.write(message.encode())
            response = self.serial.readline().decode()
            if response:
                return int(response)
            else:
                return status


def register_simfad_protocol():
    if "handler" not in serial.protocol_handler_packages:
        serial.protocol_handler_packages.append("handler")


def unregister_simfad_protocol():
    if "handler" in serial.protocol_handler_packages:
        serial.protocol_handler_packages.remove("handler")
