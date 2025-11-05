"""Simple standalone example: basic SD card operations.

Note: On simulated transport this will not touch a real card, but will show
command flow and return mock values.
"""
from pyallcode.devices.sdcard import SDCard


def main() -> None:
    sd = SDCard(verbose=1)
    try:
        print("Init:", sd.init())
        print("Create:", sd.create("demo.txt"))
        print("Open:", sd.open("demo.txt"))
        sd.write_byte(65)
        print("ReadByte:", sd.read_byte())
        print("Delete:", sd.delete("demo.txt"))
    finally:
        sd.close()


if __name__ == "__main__":
    main()
