"""IR sensors example.
Reads two IR channels (0 and 7).
"""
from pyallcode.devices.ir import IRSensors


def main() -> None:
    ir = IRSensors()
    ch0 = ir.read(0)
    ch7 = ir.read(7)
    print(f"IR[0]: {ch0}")
    print(f"IR[7]: {ch7}")


if __name__ == "__main__":
    main()
