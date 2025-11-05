"""Line sensors example.
Reads two line sensors (0 and 1).
"""
from pyallcode.devices.line import LineSensors


def main() -> None:
    line = LineSensors()
    left = line.read(0)
    right = line.read(1)
    print(f"Line[0]: {left}")
    print(f"Line[1]: {right}")


if __name__ == "__main__":
    main()
