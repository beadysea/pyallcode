# pyallcode – Formula AllCode Robot API

[![CI](https://github.com/beads/py_allcode/actions/workflows/ci.yml/badge.svg)](https://github.com/beads/py_allcode/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pyallcode.svg)](https://pypi.org/project/pyallcode/)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyallcode.svg)](https://pypi.org/project/pyallcode/)

Python API for the Formula AllCode robot.

pyallcode is a testable, and extensible Python API for the Formula AllCode robot manufactured by Matrix Tsl. It may be used as an alternative to the python API provided by Matrix Tsl.

pyallcode applies SOLID principles by separating responsibilities, using small focused interfaces, and inverting the serial dependency for easier testing.

## Installation

Install from PyPI (recommended):

```bash
pip install pyallcode
```

Latest from source for development:

```bash
pip install -e .[dev]
```

## What changed?

- The `FA.py` api provided by Matrix Tsl contains a monolithic class(`Create`) that bundles many responsibilities. Pyallcode refactors the functionality of `FA.py`into a modular framework and a new `Robot` API.
- Introduced a `pyallcode` package with clear layers:
  - Transport (serial I/O abstraction)
  - Connection (command/response mechanics)
  - Subsystems: LEDs, speaker, servo, LCD, SDCard etc.
  - Aggregator `Robot` composing all subsystems
- Cross-platform port discovery utilities moved to `pyallcode.ports` and exposed via `Robot`.

## Quick start

```python
from pyallcode import Robot

# Connect
# # attempts to autoconnect, falls back to a simulated robot
bot = Robot() 

# Use subsystems
api = bot.sensors.get_api_version()
print("API:", api)

bot.forward(200)
bot.left(90)
bot.leds.on(0) # switch on a led
bot.audio.play_note(440, 300)
front_ir = bot.ir_sensors.read(2)
print("Front IR value: ",front_ir)

bot.close()
```

## Supported Python versions

- Python 3.8 – 3.12

## SOLID alignment

- Single Responsibility: Each subsystem handles one domain (e.g., `leds`, `lcd`,`light sensor`).
- Open/Closed: New commands/subsystems can be added without modifying existing ones.
- Liskov: Subsystems expose stable, substitutable behavior; higher-level code does not rely on concrete transport.
- Interface Segregation: Small, cohesive classes; consumers use only what they need.
- Dependency Inversion: High-level code depends on `Transport` (an interface protocol), not `serial.Serial` directly.

## Port discovery (cross-platform)

```python
from pyallcode import Robot

print(Robot.list_available_ports())
print(Robot.list_ports_detailed())
print(Robot.find_robot_ports())
```

## Hardware-free simulated mode

If no serial hardware is detected (or pyserial isn't installed), the API automatically falls back to a simulated robot. This simulated robot:

- Prints acknowledgements for fire-and-forget commands (e.g., `LEDOn`, `LCDPrint`, `SetMotors`).
- Returns plausible random integers for sensor reads (e.g., `ReadIR`, `ReadLight`, `ReadMic`, `ReadAxis`, `ReadLine`), and success codes for movement/SD operations.
- Requires no hardware and no serial ports.

Optional: you can still force simulated mode explicitly by setting an environment variable before running your program (only the value 'simulated' is accepted):

**Windows PowerShell:**

```powershell
$env:PYALLCODE_TRANSPORT = "simulated"
python your_script.py
```

**Windows Command Prompt:**

```cmd
set PYALLCODE_TRANSPORT=simulated
python your_script.py
```

**Linux/macOS (Bash/Zsh):**

```bash
export PYALLCODE_TRANSPORT=simulated
python your_script.py
```

**Or run inline:**

```bash
PYALLCODE_TRANSPORT=simulated python your_script.py
```

## Standalone device usage

Each device class can now open its own serial connection. You can pass an existing `Connection` (from `Robot`) as before, or let the device auto-connect by port (or auto-detect):

```python
from pyallcode.devices.leds import LEDs
from pyallcode.devices.light import LightSensor

# Auto-detect a robot port and connect
leds = LEDs(verbose=1)               # autodetects and connects (or uses simulation)
leds.on(0)
leds.off(0)

# Connect to an explicit port
light = LightSensor(port='COM7')     # Windows; use '/dev/ttyUSB0' on Linux, '/dev/tty.usbmodem*' on macOS
print('Light:', light.read())

# Or reuse a Connection from Robot (legacy-compatible)
from pyallcode.robot import Robot
bot = Robot(autoconn=True)
mic = pyallcode.devices.mic.Mic(bot.conn)
print('Mic:', mic.read())
```

Notes:

- When no hardware is found or a port fails to open, devices fall back to the simulated transport and continue to operate for learning/testing.
- You can control verbosity by passing `verbose=0|1|2` to the device constructor.

## Running tests locally

```bash
pip install -e .[dev]
pytest -q
```

## Documentation

Sphinx docs live in `docs/`. Build them locally with:

```bash
pip install -e .[dev]
make -C docs html
```

## Releasing

1. Bump the version in `pyproject.toml` and commit.
2. Create a GitHub Release (tag matching the version).
3. GitHub Actions will build and publish to PyPI using the `PYPI_API_TOKEN` secret.
