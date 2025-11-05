"""LEDs example.
Writes a bitmask and toggles individual LEDs.
"""
from pyallcode.devices.leds import LEDs


def main() -> None:
    leds = LEDs()
    leds.write(0b00010101)
    leds.on(1)
    leds.off(2)


if __name__ == "__main__":
    main()
