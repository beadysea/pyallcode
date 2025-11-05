"""Servos example.
Enables a servo, sets positions, adjusts speed, then disables.
"""
from time import sleep
from pyallcode.devices.servos import Servos


def main() -> None:
    sv = Servos()
    sv.enable(0)
    sv.set_pos(0, 100)
    sleep(0.3)
    sv.auto_move(0, 200)
    sleep(0.3)
    sv.move_speed(50)
    sleep(0.1)
    sv.disable(0)


if __name__ == "__main__":
    main()
