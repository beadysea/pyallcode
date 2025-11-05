class FakeConnection:
    def __init__(self):
        self.calls = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return None


def test_lcd_commands():
    from pyallcode.devices.lcd import LCD

    conn = FakeConnection()
    lcd = LCD(conn)

    lcd.clear()
    lcd.print(1, 2, 'hello world')
    lcd.number(3, 4, 123)
    lcd.pixel(5, 6, 1)
    lcd.line(0, 1, 2, 3)
    lcd.rect(10, 11, 12, 13)
    lcd.backlight(1)
    lcd.options(7, 8, 1)
    lcd.verbose(0)

    cmds = [c[0] for c in conn.calls]
    assert cmds == [
        'LCDClear',
        'LCDPrint 1 2 hello world',
        'LCDNumber 3 4 123',
        'LCDPixel 5 6 1',
        'LCDLine 0 1 2 3',
        'LCDRect 10 11 12 13',
        'LCDBacklight 1',
        'LCDOptions 7 8 1',
        'LCDVerbose 0',
    ]

    # all commands are fire-and-forget
    assert all(not c[1] for c in conn.calls)
