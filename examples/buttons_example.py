"""Push buttons example.
Reads left (0) and right (1) button states.
"""
from pyallcode.devices.buttons import PushButtons


def main() -> None:
    buttons = PushButtons()
    left = buttons.read(0)
    right = buttons.read(1)
    print(f"Left button pressed: {left}")
    print(f"Right button pressed: {right}")


if __name__ == "__main__":
    main()
