class FakeConnection:
    def __init__(self):
        self.calls = []
        self.to_return = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return self.to_return.pop(0) if self.to_return else None


def test_accelerometer_reads_and_helpers():
    from pyallcode.devices.accelerometer import Accelerometer

    conn = FakeConnection()
    conn.to_return = [10, 20, 30, 40]
    acc = Accelerometer(conn)

    assert acc.read_axis(9) == 10  # raw value returned as int
    assert acc.x() == 20
    assert acc.y() == 30
    assert acc.z() == 40

    # Check commands issued
    assert conn.calls[0][0] == 'ReadAxis 9'
    assert conn.calls[1][0] == 'ReadAxis 0'
    assert conn.calls[2][0] == 'ReadAxis 1'
    assert conn.calls[3][0] == 'ReadAxis 2'
