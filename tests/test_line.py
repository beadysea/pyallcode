class FakeConnection:
    def __init__(self):
        self.calls = []
        self.to_return = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return self.to_return.pop(0) if self.to_return else None


def test_line_read():
    from pyallcode.devices.line import LineSensors

    conn = FakeConnection()
    conn.to_return = [1, 0]
    line = LineSensors(conn)

    assert line.read(0) is True
    assert line.read(1) is False

    assert conn.calls[0][0] == 'ReadLine 0'
    assert conn.calls[1][0] == 'ReadLine 1'
