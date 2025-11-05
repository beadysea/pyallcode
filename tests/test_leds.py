class FakeConnection:
    def __init__(self):
        self.calls = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return None


def test_leds_commands_formatting():
    from pyallcode.devices.leds import LEDs

    conn = FakeConnection()
    leds = LEDs(conn)

    leds.write(5)
    leds.on(1)
    leds.off(2)

    assert conn.calls == [
        ('LEDWrite 5', False, 1),
        ('LEDOn 1', False, 1),
        ('LEDOff 2', False, 1),
    ]
