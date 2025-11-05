"""pyallcode package initialization.
Provides access to the Robot class, enums, and communication port utilities.
"""
from .robot import Robot
from .enums import (
    Axis,
    Button,
    LineSensor,
    IRSensor,
)
from .comm.ports import (
    list_available_ports,
    list_ports_detailed,
    find_robot_ports,
    autodetect_robot_port,
)

__all__ = [
    "Robot",
    "AccelerometerAxis",
    "ButtonIndex",
    "LineSensorIndex",
    "IRSensorIndex",
    "list_available_ports",
    "list_ports_detailed",
    "find_robot_ports",
    "autodetect_robot_port",
]
