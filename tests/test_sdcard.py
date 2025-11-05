class FakeConnection:
    def __init__(self):
        self.calls = []
        self.to_return = []
    def execute(self, command: str, expect_response: bool = True, attempts: int = 1):
        self.calls.append((command, expect_response, attempts))
        return self.to_return.pop(0) if self.to_return else None


def test_sdcard_basic_ops():
    from pyallcode.devices.sdcard import SDCard

    conn = FakeConnection()
    conn.to_return = [1, 2, 3, 4, 5, 200]  # return values for operations
    sd = SDCard(conn)

    assert sd.init() == 1
    assert sd.create('file.txt') == 2
    assert sd.open('file.txt') == 3
    assert sd.delete('file.txt') == 4

    # write_byte sends fire-and-forget and validates input
    sd.write_byte(5)
    try:
        sd.write_byte(300)
        assert False, 'Expected ValueError for out-of-range byte'
    except ValueError:
        pass

    assert sd.read_byte() == 200

    cmds = [c[0] for c in conn.calls]
    assert cmds[:5] == [
        'CardInit',
        'CardCreate file.txt',
        'CardOpen file.txt',
        'CardDelete file.txt',
        'CardWriteByte 5',
    ]
    assert cmds[-1] == 'CardReadByte'


def test_sdcard_record_and_playback_and_bitmap():
    from pyallcode.devices.sdcard import SDCard

    conn = FakeConnection()
    conn.to_return = [10, 11, 12]
    sd = SDCard(conn)

    # record without explicit timeout uses seconds+5
    assert sd.record_mic(16, 44100, 3, 'rec.wav') == 10
    # playback default timeout
    assert sd.playback('rec.wav') == 11
    # bitmap quotes filename and strips quotes
    assert sd.bitmap(1, 2, 'image name.bmp') == 12

    assert conn.calls[0] == ('CardRecordMic 16 44100 3 rec.wav', True, 8)
    assert conn.calls[1] == ('CardPlayback rec.wav', True, 50)
    # filename quoted
    assert conn.calls[2][0] == 'CardBitmap 1 2 "image name.bmp"'
