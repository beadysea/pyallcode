import types

class FakeConnection:
    def __init__(self):
        self.calls = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return None


def test_speaker_play_note(monkeypatch):
    from pyallcode.devices.speaker import Speaker

    conn = FakeConnection()
    sp = Speaker(conn)

    slept = {'secs': 0}
    monkeypatch.setattr('time.sleep', lambda s: slept.__setitem__('secs', slept['secs'] + s))

    sp.play_note(69, 500)

    assert conn.calls == [('PlayNote 69 500', False, 1)]
    assert abs(slept['secs'] - 0.5) < 1e-9
