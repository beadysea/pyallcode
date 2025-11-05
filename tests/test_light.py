class FakeConnection:
    def __init__(self):
        self.calls = []
        self.to_return = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return self.to_return.pop(0) if self.to_return else None


def test_light_read():
    from pyallcode.devices.light import LightSensor

    conn = FakeConnection()
    conn.to_return = [321]
    sensor = LightSensor(conn)

    assert sensor.read() == 321
    assert conn.calls[0][0] == 'ReadLight'
