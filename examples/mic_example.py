"""Microphone level example.
Reads and prints the mic level.
"""
from pyallcode.devices.mic import Mic


def main() -> None:
    mic = Mic()
    value = mic.read()
    print(f"Mic level: {value}")


if __name__ == "__main__":
    main()
