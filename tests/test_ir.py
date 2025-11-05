class FakeConnection:
    def __init__(self):
        self.calls = []
        self.to_return = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return self.to_return.pop(0) if self.to_return else None


def test_ir_read():
    from pyallcode.devices.ir import IRSensors

    conn = FakeConnection()
    conn.to_return = [123, 456]
    ir = IRSensors(conn)

    assert ir.read(0) == 123
    assert ir.read(7) == 456

    assert conn.calls[0][0] == 'ReadIR 0'
    assert conn.calls[1][0] == 'ReadIR 7'
