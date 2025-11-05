class FakeConnection:
    def __init__(self):
        self.calls = []
        self.to_return = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return self.to_return.pop(0) if self.to_return else None


def test_mic_read():
    from pyallcode.devices.mic import Mic

    conn = FakeConnection()
    conn.to_return = [55]
    mic = Mic(conn)

    assert mic.read() == 55
    assert conn.calls[0][0] == 'ReadMic'
