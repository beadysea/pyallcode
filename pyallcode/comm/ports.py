"""Utilities for listing and finding communication ports.

Provides functions to list available serial ports, get detailed port information,
and find ports likely associated with robots based on description keywords.

This module also includes lightweight probing helpers to automatically identify
which serial port a robot is actually listening on. On Windows Bluetooth SPP
pairs often expose two COM ports (incoming/outgoing). Relying on names alone is
unreliable, so we provide a content-based probe that tries a short handshake and
selects the first responsive port.
"""
from typing import List, Dict, Any, Tuple, Iterable
import contextlib
import time
import serial
import serial.tools.list_ports

# A tiny, non-invasive probe command that all supported firmwares implement.
# We use GetAPIVersion as a read-only command that returns an integer.
_PROBE_COMMAND = "GetAPIVersion\n"

def list_available_ports() -> List[str]:
    """
    Lists all available serial ports.
    Returns:
        List[str]: A list of available serial port names.
    """
    return [p.device for p in serial.tools.list_ports.comports()]


def list_ports_detailed() -> List[Tuple[str, str, str]]:
    """
    Lists all available serial ports with detailed information.
    Returns:
        List[Tuple[str, str, str]]: A list of tuples containing (port name, description, hardware ID).
    """
    return [(p.device, p.description, p.hwid) for p in serial.tools.list_ports.comports()]


def find_robot_ports(description_keywords: list[str] | None = None) -> List[Dict[str, Any]]:
    """
    Finds serial ports that match specific description keywords.
    Args:
        description_keywords (list[str] | None): A list of keywords to match against port descriptions.
    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing information about matching ports.
    """
    if description_keywords is None:
        description_keywords = ['arduino', 'usb serial', 'ch340', 'cp210x', 'ftdi', 'bluetooth']
    result: List[Dict[str, Any]] = []
    for p in serial.tools.list_ports.comports():
        desc = (p.description or '').lower()
        if any(k in desc for k in description_keywords):
            result.append({
                'device': p.device,
                'description': p.description,
                'hwid': p.hwid,
            })
    return result


# -------------------- Autodetect helpers --------------------
def _score_port(desc: str, hwid: str, keywords: Iterable[str]) -> int:
    """Heuristic score for ranking candidate ports.

    Higher score means more likely to be the robot. We prioritize Bluetooth/USB
    serial keywords and the Windows BTHENUM SPP GUID when present.
    """
    s = 0
    d = (desc or "").lower()
    h = (hwid or "").lower()
    # Weighted keyword matches (earlier keyword = slightly higher weight)
    for w_idx, k in enumerate(keywords):
        if k in d:
            s += 10 * (len(list(keywords)) - w_idx)
    # Windows Bluetooth SPP GUID appears in HWID for BT serial ports
    if "bthenum" in h and "00001101-0000-1000-8000-00805f9b34fb" in h:
        s += 25
    # Generic USB serial controller patterns
    if any(x in d for x in ("usb serial", "cp210", "ch340", "ftdi")):
        s += 8
    return s


def candidate_ports(prefer_keywords: list[str] | None = None) -> List[str]:
    """Return available ports ordered by likelihood.

    Args:
        prefer_keywords: Keywords that, if present in the description, increase
            a port's score. Defaults cover common adapters and Bluetooth.

    Returns:
        List[str]: Port device names ordered best-first for probing.
    """
    if prefer_keywords is None:
        prefer_keywords = [
            # Windows friendly-name often: "Standard Serial over Bluetooth link"
            "bluetooth",
            "standard serial over bluetooth",
            # Branded names occasionally used by devices
            "allcode", "fa",  # allow matching device names like FA103608
            # Common USB UART bridges
            "cp210", "ch340", "ftdi", "usb serial",
        ]
    ports = list(serial.tools.list_ports.comports())
    print("Detected serial ports:")
    print([(p.device, p.description, p.hwid) for p in ports])
    if not ports:
        return []
    # Stable order by score desc then device name for reproducibility
    ranked = sorted(
        ports,
        key=lambda p: (
            -_score_port(getattr(p, "description", ""), getattr(p, "hwid", ""), prefer_keywords),
            str(getattr(p, "device", "")),
        ),
    )
    return [p.device for p in ranked]


def probe_port_is_robot(port: str, write_timeout: float = 0.25, read_timeout: float = 0.75) -> bool:
    """Open a port briefly and check if it responds like an AllCode robot.

    The probe sends a single GetAPIVersion command and expects a small integer
    within the timeout window. Any exceptions/timeouts are treated as a miss.
    The port is always closed before returning.
    """
    ser = None
    try:
        ser = serial.Serial(port=port, baudrate=115200, timeout=read_timeout, write_timeout=write_timeout)
        # Clear any buffered data
        _ = ser.in_waiting
        while ser.in_waiting:
            ser.readline()
        ser.write(_PROBE_COMMAND.encode())
        # Give the device a brief moment to respond
        deadline = time.time() + max(0.1, read_timeout)
        line = b""
        while time.time() < deadline:
            line = ser.readline()
            if line:
                break
        if not line:
            return False
        try:
            v = int(line.decode(errors="ignore").strip())
        except ValueError:
            return False
        # Expect a small positive API version
        return 0 <= v < 10_000
    except Exception:
        return False
    finally:
        with contextlib.suppress(Exception):
            if ser and ser.is_open:
                ser.close()


def autodetect_robot_port(prefer_keywords: list[str] | None = None,
                          max_to_probe: int | None = None,
                          per_port_timeout: float = 0.75) -> str | None:
    """Find the first serial port that behaves like the robot.

    Args:
        prefer_keywords: Optional description hint words to rank ports first.
        max_to_probe: Optional cap on how many ports to try (best-first).
        per_port_timeout: Read timeout per port used during probing.

    Returns:
        The device path (e.g. "COM7", "/dev/ttyUSB0") if found, else None.
    """
    candidates = candidate_ports(prefer_keywords)
    if max_to_probe is not None:
        candidates = candidates[:max(0, int(max_to_probe))]
    for dev in candidates:
        print(f"Probing port: {dev}")
        if probe_port_is_robot(dev, read_timeout=per_port_timeout):
            return dev
    return None
