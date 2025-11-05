class FakeConnection:
    def __init__(self):
        self.calls = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return None


def test_servos_commands():
    from pyallcode.devices.servos import Servos

    conn = FakeConnection()
    sv = Servos(conn)

    sv.enable(0)
    sv.disable(1)
    sv.set_pos(2, 150)
    sv.auto_move(3, 200)
    sv.move_speed(50)

    cmds = [c[0] for c in conn.calls]
    assert cmds == [
        'ServoEnable 0',
        'ServoDisable 1',
        'ServoSetPos 2 150',
        'ServoAutoMove 3 200',
        'ServoMoveSpeed 50',
    ]
    assert all(not c[1] for c in conn.calls)
