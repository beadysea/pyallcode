# Examples index

Run any example directly; if no serial hardware is detected, a simulator is used automatically so you can try them without a robot.

## Device examples

- `accelerometer_example.py` — print X/Y/Z axis readings
- `buttons_example.py` — read left/right push buttons (booleans)
- `ir_example.py` — read IR channels 0 and 7
- `lcd_example.py` — clear screen, print text, draw a line, set options/backlight (no console output)
- `leds_example.py` — write bitmask and toggle individual LEDs (no console output)
- `light_example.py` — read ambient light level
- `line_example.py` — read line sensors 0 and 1 (booleans)
- `mic_example.py` — read microphone level
- `servos_example.py` — enable/move/disable a servo (no console output)
- `speaker_example.py` — play a single note (no console output)
- `sdcard_example.py` — basic SD card operations (init/create/open/delete/read/write/record/playback/bitmap)
- `port_discovery_example.py` — list available serial ports and likely robot ports

## How to run (Windows PowerShell)

From the repository root:

```powershell
.\.venv\Scripts\python.exe examples\accelerometer_example.py
```

Replace `accelerometer_example.py` with any filename from above. You can also run them with your active Python if you prefer:

```powershell
python examples\buttons_example.py
```

## Selecting a specific port (optional)

All device classes support a `port` argument in their constructors. For example, to force a specific COM port in your own script:

```python
from pyallcode.devices.accelerometer import Accelerometer
acc = Accelerometer(port="COM7")
print(acc.x(), acc.y(), acc.z())
```

If the port cannot be opened, the examples fall back to the simulator and still run.
