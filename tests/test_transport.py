import types


def test_serial_transport_open_success(monkeypatch):
    import pyallcode.comm.transport as transport_mod

    class FakeSerial:
        def __init__(self, *_, port=None, **__):
            self.port = port
            self.is_open = False
            self._lines = []
        def open(self):
            self.is_open = True
        def close(self):
            self.is_open = False
        def write(self, data: bytes):
            pass
        def readline(self) -> bytes:
            return self._lines.pop(0) if self._lines else b''
        @property
        def in_waiting(self):
            return len(self._lines)

    # replace the Serial class used by SerialTransport
    monkeypatch.setattr(transport_mod.serial, 'Serial', FakeSerial)

    tr = transport_mod.SerialTransport(timeout=0.1)
    tr.open('COM5')
    assert tr.is_open is True
    assert tr.raw is not None and tr.raw.port == 'COM5'

    tr.close()
    assert tr.is_open is False


def test_serial_transport_open_failure_raises(monkeypatch):
    import pyallcode.comm.transport as transport_mod

    class FailingSerial:
        def __init__(self, *_, port=None, **__):
            self.port = port
            self.is_open = False
        def open(self):
            # does not change is_open
            pass
        def close(self):
            self.is_open = False
        def write(self, data: bytes):
            pass
        def readline(self) -> bytes:
            return b''
        @property
        def in_waiting(self):
            return 0

    monkeypatch.setattr(transport_mod.serial, 'Serial', FailingSerial)

    tr = transport_mod.SerialTransport()
    try:
        tr.open('COM6')
        assert False, 'Expected RuntimeError when failing to open'
    except RuntimeError:
        pass


def test_serial_transport_read_write_require_open(monkeypatch):
    import pyallcode.comm.transport as transport_mod

    class ClosedSerial:
        def __init__(self, *_, port=None, **__):
            self.port = port
            self.is_open = False
        def open(self):
            self.is_open = True
        def close(self):
            self.is_open = False
        def write(self, data: bytes):
            pass
        def readline(self) -> bytes:
            return b''
        @property
        def in_waiting(self):
            return 0

    monkeypatch.setattr(transport_mod.serial, 'Serial', ClosedSerial)

    tr = transport_mod.SerialTransport()
    # not open yet
    try:
        tr.write(b'x')
        assert False, 'Expected RuntimeError for write when closed'
    except RuntimeError:
        pass
    try:
        tr.readline()
        assert False, 'Expected RuntimeError for readline when closed'
    except RuntimeError:
        pass

    # open then write/read should not raise
    tr.open('COM7')
    tr.write(b'x')
    tr.readline()


def test_in_waiting_reports_zero_when_closed(monkeypatch):
    import pyallcode.comm.transport as transport_mod

    class FakeSerial:
        def __init__(self, *_, port=None, **__):
            self.port = port
            self.is_open = True
            self._lines = [b'a', b'b']
        def open(self):
            self.is_open = True
        def close(self):
            self.is_open = False
        def write(self, data: bytes):
            pass
        def readline(self) -> bytes:
            return self._lines.pop(0) if self._lines else b''
        @property
        def in_waiting(self):
            return len(self._lines)

    monkeypatch.setattr(transport_mod.serial, 'Serial', FakeSerial)

    tr = transport_mod.SerialTransport()
    # closed => 0
    assert tr.in_waiting == 0

    tr.open('COM8')
    assert tr.in_waiting == 2
    tr.readline()
    assert tr.in_waiting == 1
