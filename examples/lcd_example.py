"""LCD example.
Clears, prints text, draws a line and toggles backlight.
"""
from pyallcode.devices.lcd import LCD


def main() -> None:
    lcd = LCD()
    lcd.clear()
    lcd.print(0, 0, "Hello, AllCode!")
    lcd.line(0, 10, 50, 10)
    lcd.backlight(1)
    lcd.options(1, 0, 1)  # example options: fg=1, bg=0, transparent=1


if __name__ == "__main__":
    main()
