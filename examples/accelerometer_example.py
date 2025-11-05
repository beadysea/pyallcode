"""Accelerometer example.
Runs without hardware by auto-connecting or falling back to a simulator.
"""
from pyallcode.devices.accelerometer import Accelerometer


def main() -> None:
    acc = Accelerometer()  # auto-connect or simulate
    print("Accelerometer readings:")
    print(f"  X: {acc.x()}")
    print(f"  Y: {acc.y()}")
    print(f"  Z: {acc.z()}")


if __name__ == "__main__":
    main()
