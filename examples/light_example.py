"""Ambient light sensor example.
Reads and prints the light level.
"""
from pyallcode.devices.light import LightSensor


def main() -> None:
    sensor = LightSensor()
    value = sensor.read()
    print(f"Light: {value}")


if __name__ == "__main__":
    main()
