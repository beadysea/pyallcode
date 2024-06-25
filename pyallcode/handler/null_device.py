"""A null serial device that simulates communication between the allcode api and a flowcode device.
    """

from random import randint

# from random import randrange


class Nullserial:
    def __init__(self):
        self.is_open = False
        self.response = ""
        self.commands = [
            "GetAPIVersion",
            "GetBattery",
            "Forwards",
            "Backwards",
            "Left",
            "Right",
            "SetMotors",
            "ReadAxis",
            "ReadSwitch",
            "ReadIR",
            "LCDClear",
            "LCDPrint",
            "LCDNumber",
            "LCDPixel",
            "LCDLine",
            "LCDRect",
            "CardBitmap",
            "LCDBacklight",
            "LCDOptions",
            "LEDWrite",
            "LEDOn",
            "LEDOff",
            "ReadLight",
            "ReadLine",
            "ReadMic",
            "CardInit",
            "CardCreate",
            "CardOpen",
            "CardDelete",
            "CardWriteByte",
            "CardReadByte",
            "CardRecordMic",
            "CardPlayBack",
            "ServoEnable",
            "ServoDisable",
            "ServoSetPos",
            "ServoAutoMove",
            "ServoMoveSpeed",
            "PlayNote",
        ]
        print("Null serial device instantiated")

    def __enter__(self):
        if not self.is_open:
            self.is_open = True

    def __exit__(self, *args):
        if not self.is_open:
            self.is_open = False

    def close(self):
        if self.is_open:
            self.is_open = False

    def write(self, data: bytes) -> int:
        message = data.decode().split()
        command = message[0]
        if command not in self.commands:
            return len(data)
        operands = [int(message[i]) for i in range(1, len(message))]
        self.execute(command, operands)
        return len(data)

        return len(data)

    def readline(self, size: int | None = -1) -> bytes:
        if size is None:
            return bytes()
        response = self.response.encode()
        print(response)
        self.response = ""
        return response

    def execute(self, command: str, operands: list[int]) -> None:

        if command == "GetAPIVersion":
            self.response = "1"
        if command == "GetBattery":
            self.response = str(randint(0, 500))

        if command == "ReadAxis":
            self.response = str(randint(-32768, 32768))
        if command == "ReadSwitch":
            self.response = str(randint(0, 1))
        if command == "ReadLine":
            self.response = str(randint(0, 200))
        if command == "ReadIR" or "ReadLight" or "ReadMic":
            self.response = str(randint(0, 4095))

        if command == "Forwards":
            print("Null serial: moving forward ", operands[0], "mm")
        if command == "Backwards":
            print("Null serial: moving backward ", operands[0], "mm")
        if command == "Left":
            print("Null serial: turning left ", operands[0], "degrees")
        if command == "Right":
            print("Null serial: turning right ", operands[0], "degrees")
        if command == "SetMotors":
            print("Null serial: left motor ", operands[0], "right motor", operands[1])

        if command == "LCDClear":
            print("Null serial: LCD Clear")
        if command == "LCDPrint":
            print("Null serial: LCD Number", operands[-1])
        if command == "LCDNumber":
            print("Null serial: LCD Number", operands[-1])

        if command == "LEDWrite":
            print("Null serial: LED Write", bin(operands[0]), "degrees")
        if command == "LEDOn":
            print("Null serial: LED ", operands[0], "on")
        if command == "LEDOff":
            print("Null serial: LED ", operands[0], "off")

    @property
    def in_waiting(self) -> int:
        return 0
