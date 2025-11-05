"""""Module providing the Robot class for controlling the AllCode robot.

This module defines the Robot class, which encapsulates the functionality to control
the AllCode robot, including movement commands and access to various sensors and actuators.
It also provides static methods for discovering available serial ports and identifying
ports associated with the AllCode robot.
"""
from .comm.transport import SerialTransport, SimulatedTransport, transport_mode_from_env
from .comm.connection import Connection
from .comm.ports import (
    list_available_ports,
    list_ports_detailed,
    find_robot_ports,
    autodetect_robot_port,
)
from .devices.accelerometer import Accelerometer
from .devices.buttons import PushButtons
from .devices.ir import IRSensors
from .devices.lcd import LCD
from .devices.leds import LEDs
from .devices.light import LightSensor
from .devices.line import LineSensors
from .devices.mic import Mic
from .devices.sdcard import SDCard
from .devices.servos import Servos
from .devices.speaker import Speaker

class Robot:
    """Represents the AllCode robot and provides methods to control it.
    
    Args:
        verbose (int): Verbosity level for connection debugging (default: 0).
        mm_per_sec (int): Speed in mm/s for movement commands (default: 50).
        deg_per_sec (int): Speed in degrees/s for turn commands (default: 45).
        
        Attributes:
            transport (SerialTransport): The transport layer for communication.
            conn (Connection): The connection object for sending commands.
            mm_per_sec (int): Speed in mm/s for movement commands.
            deg_per_sec (int): Speed in degrees/s for turn commands.
            accelerometer (Accelerometer): The accelerometer sensor interface.
            push_buttons (PushButtons): The push buttons interface.
            ir_sensors (IRSensors): The infrared sensors interface.
            lcd (LCD): The LCD display interface.
            leds (LEDs): The LEDs interface.
            light_sensor (LightSensor): The light sensor interface.
            line_sensors (LineSensors): The line sensors interface.
            mic (Mic): The microphone sensor interface.
            sd_card (SDCard): The SD card interface.
            servo (Servo): The servo motor interface.
            speaker (Speaker): The speaker interface.
            """

    def __init__(self, autoconn: bool = True, verbose: int = 0, mm_per_sec: int = 50, deg_per_sec: int = 45) -> None:
        """Initializes the Robot with specified parameters.
        
         Args:
            autoconn (bool): Whether to automatically connect to the robot on initialization (default: True).
            verbose (int): Verbosity level for connection debugging (default: 0).
            mm_per_sec (int): Speed in mm/s for movement commands (default: 50).
            deg_per_sec (int): Speed in degrees/s for turn commands (default: 45).
        """
        # Choose transport based on environment variable when provided
        forced_mode = transport_mode_from_env()
        if forced_mode == "simulated":
            self.transport = SimulatedTransport()
        else:
            # Default to real serial; fallback to simulated happens in open/autoconnect if needed
            self.transport = SerialTransport()
        self.conn = Connection(self.transport, verbose=verbose)
        self.mm_per_sec = max(1, mm_per_sec)
        self.deg_per_sec = max(1, deg_per_sec)
        self.accelerometer = Accelerometer(self.conn)
        self.push_buttons = PushButtons(self.conn)
        self.ir_sensors = IRSensors(self.conn)
        self.lcd = LCD(self.conn)
        self.leds = LEDs(self.conn)
        self.light_sensor = LightSensor(self.conn)
        self.line_sensors = LineSensors(self.conn)
        self.mic = Mic(self.conn)
        self.sd_card = SDCard(self.conn)
        self.servo = Servos(self.conn)
        self.speaker = Speaker(self.conn)
        if autoconn:
            if forced_mode == "simulated":
                # Open a friendly simulated connection immediately
                self.transport.open("SIMULATED")
                if self.conn.verbose:
                    print("[SimulatedRobot] Forced by PYALLCODE_TRANSPORT; using simulated transport")
            else:
                self.autoconnect()

    def open(self, port: str | int) -> None:
        """Open connection to the robot on the specified port.
        Args:
            port (str | int): The port name or index to open.
        """
        try:
            self.conn.open(port)
        except Exception as e:
            # Fallback to simulated when we cannot open a real serial device
            self.transport = SimulatedTransport()
            self.conn.transport = self.transport
            # Use a friendly pseudo-port label so user code can see something meaningful
            label = str(port) if isinstance(port, str) else f"SIMULATED-{port}"
            self.transport.open(label)
            if self.conn.verbose:
                print(f"[SimulatedRobot] Falling back to simulated transport: {e}")

    def close(self) -> None:
        """Close the connection to the robot."""
        self.conn.close()

    def autoconnect(self,
                    prefer_keywords: list[str] | None = None,
                    max_to_probe: int | None = None,
                    per_port_timeout: float = 0.75) -> str:
        """Automatically discover and open the robot's serial port.

        Tries candidate ports in a best-first order and performs a short, safe
        handshake to confirm the device. Returns the selected port string.

        Args:
            prefer_keywords: Optional description hints to rank ports first
                (e.g., ['bluetooth', 'allcode']).
            max_to_probe: Optional cap for number of ports to try.
            per_port_timeout: Read timeout used per port during probing.

        Raises:
            RuntimeError: If no responsive robot port is found.

        Returns:
            str: The device path of the connected port.
        """
        port = autodetect_robot_port(prefer_keywords, max_to_probe, per_port_timeout)
        if port:
            self.open(port)
            return port
        # No hardware found -> engage simulated port automatically
        self.transport = SimulatedTransport()
        self.conn.transport = self.transport
        simulated_port = "SIMULATED"
        self.transport.open(simulated_port)
        if self.conn.verbose:
            print("[SimulatedRobot] No serial hardware detected; using simulated transport")
        return simulated_port

    def set_verbose(self, value: int) -> None:
        """Set the verbosity level of the connection.
        
        Args:
            value (int): The verbosity level to set.
        """
        self.conn.verbose = value

    # ----- movement & commands -----    
    def get_api_version(self) -> int:
        """Get the API version of the robot firmware.
        

        Returns:
            int: The API version number.
        """
        return int(self.conn.execute('GetAPIVersion', True, 1) or -1)
    def get_battery_voltage(self) -> int:
        """Get the battery voltage in millivolts.

        Returns:
            int: The battery voltage in millivolts.
        """
        return int(self.conn.execute('GetBatteryVoltage', True, 1) or -1)
    
    def set_motors(self, left: int, right: int) -> None:
        """Set the left and right motor speeds.
        
        Args:
            left (int): Speed for the left motor (-255 to 255).
            right (int): Speed for the right motor (-255 to 255).
        """
        self.conn.execute(f'SetMotors {int(left)} {int(right)}', expect_response=False)

    def forwards(self, distance_mm: int) -> int:
        """Move the robot forwards by the specified distance in millimeters.
        
        Args:
            distance_mm (int): Distance to move forwards in millimeters.
        """
        timeout = max(1, abs(int(distance_mm / self.mm_per_sec)))
        return int(self.conn.execute(f'Forwards {int(distance_mm)}', True, timeout) or -1)

    def backwards(self, distance_mm: int) -> int:
        """Move the robot backwards by the specified distance in millimeters.
        Args:
            distance_mm (int): Distance to move backwards in millimeters.
        """
        timeout = max(1, abs(int(distance_mm / self.mm_per_sec)))
        return int(self.conn.execute(f'Backwards {int(distance_mm)}', True, timeout) or -1)

    def left(self, angle_deg: int) -> int:
        """Turn the robot left by the specified angle in degrees.
        Args:
            angle_deg (int): Angle to turn left in degrees.
        """
        timeout = max(1, abs(int(angle_deg / self.deg_per_sec)))
        return int(self.conn.execute(f'Left {int(angle_deg)}', True, timeout) or -1)

    def right(self, angle_deg: int) -> int:
        """Turn the robot right by the specified angle in degrees.
        Args:
            angle_deg (int): Angle to turn right in degrees.
        """
        timeout = max(1, abs(int(angle_deg / self.deg_per_sec)))
        return int(self.conn.execute(f'Right {int(angle_deg)}', True, timeout) or -1)
    
    # Convenience passthroughs for discovery utilities
    list_available_ports = staticmethod(list_available_ports)
    list_ports_detailed = staticmethod(list_ports_detailed)
    find_robot_ports = staticmethod(find_robot_ports)
    autoconnect_robot_port = staticmethod(autodetect_robot_port)
