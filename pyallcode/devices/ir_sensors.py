from pyallcode.serial_comms import CommunicationDevice

MIN_IR_SENSOR = 0
MAX_IR_SENSOR = 7


class IRSensors:
    def __init__(self, device: CommunicationDevice) -> None:
        self.device = device

    def read(self, sensor: int) -> int:
        """Reads the value of the given sensor.

        Args:
            sensor (int): Number of sensor to read between 0 and 7

        Raises:
            ValueError: when the sensor number is out of range.

        Returns:
            int: the value of the given sensor.
        """
        if sensor not in range(MIN_IR_SENSOR, MAX_IR_SENSOR + 1):
            raise ValueError(
                "Invalid sensor value {sensor}. "
                "Sensor value must be in the range {MIN_IR_SENSOR} to {MAX_IR_SENSOR}.".format(
                    sensor=sensor,
                    MIN_IR_SENSOR=MIN_IR_SENSOR,
                    MAX_IR_SENSOR=MAX_IR_SENSOR,
                )
            )

        command = f"ReadIR {sensor}\n"
        return self.device.send_message(command)
