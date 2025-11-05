"""Common base providing optional self-managed serial connection for devices.

This mixin/base lets each device be used either:

- With an existing Connection provided by the Robot (backward compatible)
- Or standalone by auto-creating and opening its own serial connection

Usage pattern inside device classes:

    class LEDs(DeviceBase):
        def __init__(self, conn: Connection | None = None, port: str | int | None = None,
                     autoconn: bool = True, verbose: int = 0) -> None:
            super().__init__(conn=conn, port=port, autoconn=autoconn, verbose=verbose)
            # device methods can now use self.conn
"""

from __future__ import annotations

from typing import Optional

from ..comm.connection import Connection
from ..comm.transport import SerialTransport, SimulatedTransport, transport_mode_from_env
from ..comm.ports import autodetect_robot_port


class DeviceBase:
    """Provide a Connection for device classes.

    Args:
        conn: Existing Connection to use (e.g., from Robot). If provided, it's used as-is.
        port: Serial port to open if creating our own connection. Can be a COM index/int
              or a full device path string. If omitted, an autodetect probe will be used.
        autoconn: When True (default), open the connection immediately (or fall back to
                  a simulated transport if no hardware is detected). When False, users can
                  call `.open(port)` later.
        verbose: Verbosity forwarded to the Connection.
    """

    def __init__(
        self,
        conn: Optional[Connection] = None,
        port: Optional[str | int] = None,
        autoconn: bool = True,
        verbose: int = 0,
    ) -> None:
        # If a connection is supplied (Robot path), keep legacy behavior.
        if conn is not None:
            self.conn = conn
            return

        # Otherwise create our own connection (standalone device usage).
        forced_mode = transport_mode_from_env()
        if forced_mode == "simulated":
            transport = SimulatedTransport()
            self.conn = Connection(transport, verbose=verbose)
            if autoconn:
                label = "SIMULATED" if port is None else (str(port) if isinstance(port, str) else f"SIMULATED-{port}")
                transport.open(label)
                if getattr(self.conn, "verbose", 0):
                    print("[SimulatedRobot] Forced by PYALLCODE_TRANSPORT; using simulated transport")
        else:
            transport = SerialTransport()
            self.conn = Connection(transport, verbose=verbose)
            if autoconn:
                self._open_with_fallback(port)

    # ----- lifecycle helpers -----
    def open(self, port: str | int | None = None) -> str:
        """Open the device connection on a chosen or auto-detected port.

        Returns the connected port label (real device path or 'SIMULATED').
        """
        return self._open_with_fallback(port)

    def close(self) -> None:
        """Close the underlying connection."""
        self.conn.close()

    def set_verbose(self, value: int) -> None:
        """Set Connection verbosity."""
        self.conn.verbose = value

    # ----- internals -----
    def _open_with_fallback(self, port: str | int | None) -> str:
        # Honor forced simulated mode via environment variable first.
        if transport_mode_from_env() == "simulated":
            sim = SimulatedTransport()
            self.conn.transport = sim
            label = "SIMULATED" if port is None else (str(port) if isinstance(port, str) else f"SIMULATED-{port}")
            sim.open(label)
            if getattr(self.conn, "verbose", 0):
                print("[SimulatedRobot] Forced by PYALLCODE_TRANSPORT; using simulated transport")
            return label

        # Try the requested or auto-detected real serial first.
        chosen_port: Optional[str]
        try:
            if port is None:
                chosen_port = autodetect_robot_port()
                if chosen_port:
                    self.conn.open(chosen_port)
                    return chosen_port
                raise RuntimeError("No responsive robot port found")
            else:
                self.conn.open(port)
                return str(port)
        except Exception as e:
            # Fall back to a simulated device so examples/tests can run without hardware.
            sim = SimulatedTransport()
            self.conn.transport = sim
            label = "SIMULATED" if port is None else (str(port) if isinstance(port, str) else f"SIMULATED-{port}")
            sim.open(label)
            if getattr(self.conn, "verbose", 0):
                print(f"[SimulatedRobot] DeviceBase: using simulated transport: {e}")
            return label
