from pyallcode.devices.push_buttons import PushButtons
from pyallcode.enums import Button
from pyallcode.serial_comms import SerialDevice

push_buttons: PushButtons = PushButtons(SerialDevice())
left_button: bool = push_buttons.read(Button.LEFT)
right_button: bool = push_buttons.read(Button.RIGHT)
print(f"Left Button: {left_button}")
print(f"Right Button: {right_button}")
