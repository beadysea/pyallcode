import sys
import types
import pytest

# Provide a stub 'serial' module if pyserial isn't installed so imports don't fail.
if 'serial' not in sys.modules:
    serial_stub = types.ModuleType('serial')

    # Minimal attributes used by code
    serial_stub.PARITY_NONE = object()
    serial_stub.STOPBITS_ONE = object()
    serial_stub.EIGHTBITS = object()

    class _DefaultFakeSerial:
        def __init__(self, *_, port=None, **__):
            self.port = port
            self.is_open = True
            self._in_waiting = 0
            self._writes = []
            self._lines = []
        def open(self):
            self.is_open = True
        def close(self):
            self.is_open = False
        def write(self, data: bytes):
            if not self.is_open:
                raise RuntimeError('Serial port is not open')
            self._writes.append(bytes(data))
        def readline(self) -> bytes:
            if not self.is_open:
                raise RuntimeError('Serial port is not open')
            return self._lines.pop(0) if self._lines else b''
        @property
        def in_waiting(self) -> int:
            return len(self._lines)

    serial_stub.Serial = _DefaultFakeSerial

    # serial.tools.list_ports.comports shim
    tools_mod = types.ModuleType('serial.tools')
    list_ports_mod = types.ModuleType('serial.tools.list_ports')

    def _default_comports():
        return []

    list_ports_mod.comports = _default_comports
    tools_mod.list_ports = list_ports_mod

    serial_stub.tools = tools_mod

    sys.modules['serial'] = serial_stub
    sys.modules['serial.tools'] = tools_mod
    sys.modules['serial.tools.list_ports'] = list_ports_mod


class DummyTransport:
    """A test double for Transport interface used by Connection tests."""
    def __init__(self):
        self.opened_with = None
        self.closed = False
        self._writes = []
        self._lines = []  # queue of bytes to return from readline
    def open(self, port: str) -> None:
        self.opened_with = port
        self.closed = False
    def close(self) -> None:
        self.closed = True
    def write(self, data: bytes) -> None:
        if self.closed:
            raise RuntimeError('transport closed')
        self._writes.append(bytes(data))
    def readline(self) -> bytes:
        if self.closed:
            raise RuntimeError('transport closed')
        return self._lines.pop(0) if self._lines else b''
    @property
    def in_waiting(self) -> int:
        return len(self._lines)
    @property
    def is_open(self) -> bool:
        return not self.closed


@pytest.fixture
def dummy_transport():
    return DummyTransport()
