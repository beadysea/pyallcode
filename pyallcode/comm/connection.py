"""Manages the connection to the device over a specified transport layer."""
from typing import Optional
from sys import platform
from .transport import Transport, SimulatedTransport

class Connection:
    """Manages communication with the device over a given transport.
    Args:
        transport (Transport): The transport layer to use for communication.
        verbose (int, optional): Verbosity level (0 = no output, 1 = some output, 2 = debug output).
    """

    def __init__(self, transport: Transport, verbose: int = 0) -> None:
        """Initializes the Connection with a transport and verbosity level."""
        self.transport = transport
        self.verbose = verbose

    def open(self, port: str | int) -> None:
        """Opens the connection on the specified port.
        Args:
            port (str | int): The port to open.
        """
        s: str
        if isinstance(port, int) or (isinstance(port, str) and port.isdigit()):
            if platform in ("linux", "linux2"):
                s = f"/dev/rfcomm{port}"
            elif platform == "darwin":
                s = f"/dev/tty.{port}-Port"
            elif platform == "win32":
                s = f"\\\\.\\COM{port}"
            else:
                raise ValueError("Unsupported platform")
        else:
            s = str(port)
        self.transport.open(s)
        if self.verbose:
            print(f"Connected on {s}")

    def close(self) -> None:
        """Closes the connection."""
        self.transport.close()

    def flush_input(self) -> None:
        """Flushes the input buffer to remove any stale data."""
        # Drain input buffer
        while self.transport.in_waiting > 0:
            self.transport.readline()

    def send(self, command: str) -> None:
        """Sends a command to the device.
        Args:
            command (str): The command to send.
        """
        if self.verbose:
            print(f"-> {command.strip()}")
        self.transport.write(command.encode())

    def read_value(self, label: str, attempts: int = 1) -> int:
        """Reads an integer value from the device.
        Args:
            label (str): The label for the value being read.
            attempts (int, optional): The number of attempts to read the value.
        
        Returns:
            int: The integer value read from the device, or -1 if unsuccessful.
            
            raises: ValueError: If the read value cannot be converted to an integer.
        """
        val = -1
        for i in range(max(1, attempts)):
            try:
                line = self.transport.readline().decode(errors="ignore").strip()
                if line:
                    val = int(line)
                    if self.verbose:
                        print(f"<- {label}: {val}")
                    return val
            except ValueError:
                if self.verbose:
                    print(f"<- {label}: no valid int (attempt {i+1})")
        return val

    def execute(self, command: str, expect_response: bool = True, attempts: int = 1) -> int | None:
        """Executes a command on the device and optionally reads a response.
        
        Args:
            command (str): The command to execute.
            expect_response (bool, optional): Whether to expect a response from the device.
            attempts (int, optional): The number of attempts to read the response.
            
            Returns:
                int | None: The integer response from the device, or None if no response is expected.
        """
        self.flush_input()
        self.send(command if command.endswith("\n") else command + "\n")
        if expect_response:
            return self.read_value(command.split()[0], attempts)
        # In dummy mode, print a friendly acknowledgement for fire-and-forget commands
        if isinstance(self.transport, SimulatedTransport):
            print(f"[SimulatedRobot] OK: {command.strip()}")
        return None
