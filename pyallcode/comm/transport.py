"""Defines transport layer classes for communication.
Provides a Transport protocol (interface), a SerialTransport implementation
using pyserial, and a SimulatedTransport for hardware-free simulation.
"""
from typing import Optional, Protocol, runtime_checkable
import os
import random
import time

# pyserial is optional for users running in dummy mode. Import lazily/safely.
try:
    import serial  # type: ignore
except Exception:  # pragma: no cover - exercised in real installs without pyserial
    class _SerialShim:  # minimal attributes so type annotations/imports don't explode
        PARITY_NONE = object()
        STOPBITS_ONE = object()
        EIGHTBITS = object()
        class Serial:  # accessing this without pyserial should clearly fail
            def __init__(self, *a, **k):
                raise ImportError("pyserial is required for SerialTransport; set PYALLCODE_TRANSPORT=simulated for simulated mode")
    serial = _SerialShim()  # type: ignore

@runtime_checkable
class Transport(Protocol):
    """Transport interface for communication layers.

    Any class that implements these members is considered a Transport.
    """
    def open(self, port: str) -> None: ...
    def close(self) -> None: ...
    def write(self, data: bytes) -> None: ...
    def readline(self) -> bytes: ...
    @property
    def in_waiting(self) -> int: ...
    @property
    def is_open(self) -> bool: ...

class SerialTransport:
    """Serial transport implementation using pyserial.
    Args:
        baudrate (int): The baud rate for the serial connection.
        parity (serial.Parity): The parity setting for the serial connection.
        stopbits (serial.StopBits): The stop bits setting for the serial connection.
        bytesize (serial.ByteSize): The byte size setting for the serial connection.
    """
    def __init__(self,
                 baudrate: int = 115200,
                 parity = serial.PARITY_NONE,
                 stopbits = serial.STOPBITS_ONE,
                 bytesize = serial.EIGHTBITS,
                 timeout: Optional[float] = 1.0) -> None:
        self._serial: Optional[object] = None
        self._config = dict(
            baudrate=baudrate,
            parity=parity,
            stopbits=stopbits,
            bytesize=bytesize,
            timeout=timeout,
        )

    def open(self, port: str) -> None:
        """Opens the serial port.
        Args:
            port (str): The serial port to open.
        """
        if self._serial and self._serial.is_open:
            self._serial.close()
        self._serial = serial.Serial(port=port, **self._config)
        if not self._serial.is_open:
            self._serial.open()
        if not self._serial.is_open:
            raise RuntimeError(f"Failed to open serial port: {port}")

    def close(self) -> None:
        """Closes the serial port."""
        if self._serial and self._serial.is_open:
            self._serial.close()

    def write(self, data: bytes) -> None:
        """Writes data to the serial port.
        Args:
            data (bytes): The data to write.
        """
        if not self._serial or not self._serial.is_open:
            raise RuntimeError("Serial port is not open")
        self._serial.write(data)

    def readline(self) -> bytes:
        """Reads a line of data from the serial port.
        Returns:
            bytes: The line of data read.
        """
        if not self._serial or not self._serial.is_open:
            raise RuntimeError("Serial port is not open")
        return self._serial.readline()

    @property
    def in_waiting(self) -> int:
        """Returns the number of bytes in the input buffer."""
        if not self._serial or not self._serial.is_open:
            return 0
        return self._serial.in_waiting

    @property
    def is_open(self) -> bool:
        """Returns whether the serial port is open."""
        return bool(self._serial and self._serial.is_open)

    @property
    def raw(self) -> Optional[object]:
        """Returns the raw serial object."""
        return self._serial


class SimulatedTransport:
    """A hardware-free transport that simulates the robot.

    Behavior:
    - open/close simply toggle an internal flag.
    - write() records the last command and prints a user-friendly message.
    - readline() synthesizes a plausible integer response based on the last
      command and returns it as a newline-terminated bytes string.
    - in_waiting is always 0 (no buffering needed).

    This transport enables students to run code without any hardware. For
    commands that don't expect a reply, an acknowledgement is printed by the
    Connection layer when it detects this transport.
    """

    def __init__(self) -> None:
        self._is_open = False
        self._last_command: str | None = None
        self._connected_port: Optional[str] = None

    def open(self, port: str) -> None:
        self._is_open = True
        self._connected_port = port
        print(f"[SimulatedRobot] Connected (simulated) on {port}")

    def close(self) -> None:
        if self._is_open:
            print("[SimulatedRobot] Disconnected")
        self._is_open = False

    def _echo_command(self, cmd: str | None) -> int:
        """Prints a user-friendly echo of certain commands."""
        head = (cmd or "").split()[0]
        if head in ["Forwards", "Backwards", "Left", "Right",
                    "CardInit", "CardCreate", "CardOpen", "CardDelete"]:
            # Avoid overly chatty output; leave acknowledgements to Connection
            print(f"-> [SimulatedRobot] {cmd}")
    
    def write(self, data: bytes) -> None:
        if not self._is_open:
            raise RuntimeError("Simulated transport is not open")
        try:
            cmd = data.decode(errors="ignore").strip()
        except Exception:
            cmd = ""
        self._last_command = cmd
        # Light echo to help students see what was sent
        self._echo_command(cmd)
            
    def _random_for_command(self, cmd: str | None) -> int:
        head = (cmd or "").split()[0]
        # Deterministic-ish seed per call to avoid identical bursts while
        # remaining unpredictable across different commands.
        random.seed(time.time_ns() ^ hash(cmd))
        if head == "GetAPIVersion":
            return 7
        if head == "GetBatteryVoltage":
            return random.randint(0, 5000)
        if head == "ReadAxis":  # accelerometer XYZ
            return random.randint(-32768, 32768)
        if head == "ReadSwitch":  # buttons
            return random.randint(0, 1)
        if head == "ReadIR":
            return random.randint(0, 4095)
        if head == "ReadLight":
            return random.randint(0, 4095)
        if head == "ReadLine":
            return random.randint(0, 1)
        if head == "ReadMic":
            return random.randint(1, 4095)
        if head in ("Forwards", "Backwards", "Left", "Right"):
            # Movement complete/ack
            return 1
        if head in ("CardInit", "CardCreate", "CardOpen", "CardDelete",
                    "CardRecordMic", "CardPlayback", "CardBitmap"):
            return 1
        if head == "CardReadByte":
            return random.randint(0, 255)
        # Default: benign OK
        return 1

    def readline(self) -> bytes:
        if not self._is_open:
            raise RuntimeError("Simulated transport is not open")
        val = self._random_for_command(self._last_command)
        return f"{val}\n".encode()

    @property
    def in_waiting(self) -> int:
        return 0

    @property
    def is_open(self) -> bool:
        return self._is_open


# -------------------- helpers --------------------


# -------------------- helpers --------------------
def transport_mode_from_env() -> Optional[str]:
    """Return 'simulated' if PYALLCODE_TRANSPORT is exactly 'simulated' (case-insensitive).

    Any other value (including legacy 'null' or 'dummy') is ignored.
    Returns None when unset or not 'simulated'.
    """
    val = os.environ.get("PYALLCODE_TRANSPORT")
    if val and val.strip().lower() == "simulated":
        return "simulated"
    return None
