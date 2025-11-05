import types
from tests.conftest import DummyTransport


def test_open_windows_int_port(monkeypatch):
    from pyallcode.comm import connection
    t = DummyTransport()
    conn = connection.Connection(t)
    monkeypatch.setattr(connection, 'platform', 'win32')

    conn.open(3)
    assert t.opened_with == r"\\.\COM3"


def test_open_windows_digit_str_port(monkeypatch):
    from pyallcode.comm import connection
    t = DummyTransport()
    conn = connection.Connection(t)
    monkeypatch.setattr(connection, 'platform', 'win32')

    conn.open('7')
    assert t.opened_with == r"\\.\COM7"


def test_open_linux_rfcomm(monkeypatch):
    from pyallcode.comm import connection
    t = DummyTransport()
    conn = connection.Connection(t)
    monkeypatch.setattr(connection, 'platform', 'linux')

    conn.open(0)
    assert t.opened_with == "/dev/rfcomm0"


def test_open_darwin_tty(monkeypatch):
    from pyallcode.comm import connection
    t = DummyTransport()
    conn = connection.Connection(t)
    monkeypatch.setattr(connection, 'platform', 'darwin')

    # digit string should map to /dev/tty.<port>-Port on darwin
    conn.open('123')
    assert t.opened_with == "/dev/tty.123-Port"


def test_open_with_full_string(monkeypatch):
    from pyallcode.comm import connection
    t = DummyTransport()
    conn = connection.Connection(t)
    monkeypatch.setattr(connection, 'platform', 'win32')

    conn.open('COM12')
    assert t.opened_with == 'COM12'


def test_open_unsupported_platform(monkeypatch):
    from pyallcode.comm import connection
    t = DummyTransport()
    conn = connection.Connection(t)
    monkeypatch.setattr(connection, 'platform', 'weirdos')

    try:
        conn.open(1)
        assert False, 'Expected ValueError'
    except ValueError:
        pass


def test_flush_input_drains_buffer():
    from pyallcode.comm.connection import Connection
    t = DummyTransport()
    # Preload three lines
    t._lines = [b'1\n', b'2\n', b'3\n']
    conn = Connection(t)
    conn.flush_input()
    assert t.in_waiting == 0


def test_send_and_execute_adds_newline_and_reads_int(monkeypatch):
    from pyallcode.comm.connection import Connection
    t = DummyTransport()
    conn = Connection(t, verbose=0)

    # Avoid draining by flush_input in this test
    monkeypatch.setattr(Connection, 'flush_input', lambda self: None)
    # Queue one valid integer line that will be read after the write
    t._lines = [b'42\n']
    out = conn.execute('TestCommand 1 2', expect_response=True, attempts=1)

    # Check newline was appended to the write
    assert t._writes[-1].endswith(b"\n")
    assert out == 42


def test_read_value_invalid_then_valid(monkeypatch):
    from pyallcode.comm.connection import Connection
    t = DummyTransport()
    conn = Connection(t)

    # invalid, then valid
    t._lines = [b'nope\n', b'7\n']
    assert conn.read_value('Label', attempts=2) == 7


def test_read_value_all_invalid_returns_minus_one():
    from pyallcode.comm.connection import Connection
    t = DummyTransport()
    conn = Connection(t)

    t._lines = [b'bad\n', b'also bad\n']
    assert conn.read_value('Label', attempts=2) == -1
