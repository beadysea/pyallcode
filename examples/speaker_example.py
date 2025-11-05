"""Speaker example.
Plays a single note for half a second.
"""
from pyallcode.devices.speaker import Speaker


def main() -> None:
    sp = Speaker()
    sp.play_note(69, 500)  # A4 (MIDI 69), 500 ms


if __name__ == "__main__":
    main()
