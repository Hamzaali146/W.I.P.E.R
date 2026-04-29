#!/usr/bin/env python3
"""Serial transport for the STM32 laser controller link.

Implements the framed ASCII protocol used by the STM32 firmware:

    $<payload>*<CS>\\n

where CS is a two-char uppercase hex XOR checksum of the payload bytes
between '$' and '*'. Mode DRY_RUN logs every outgoing packet and skips
I/O; mode LIVE opens pyserial and reconnects on failure.
"""

from __future__ import annotations

import time
from typing import List, Optional

try:
    import serial
    from serial import SerialException
except ImportError:  # pragma: no cover - only hit when pyserial absent
    serial = None

    class SerialException(Exception):
        """Fallback so type checks don't fail when pyserial is missing."""


def xor_checksum(payload: str) -> int:
    """XOR of all ASCII bytes in the payload (between '$' and '*')."""
    value = 0
    for byte in payload.encode("ascii", errors="ignore"):
        value ^= byte
    return value


def frame_packet(payload: str) -> str:
    """Wrap a payload string as `$PAYLOAD*CS\\n`."""
    return f"${payload}*{xor_checksum(payload):02X}\n"


def format_mm(value_mm: float) -> str:
    """Format a millimeter value as `.1f` (e.g. -37.5, 0.0, 105.0)."""
    return f"{value_mm:.1f}"


def build_arm(state: bool) -> str:
    return frame_packet(f"ARM,{1 if state else 0}")


def build_offset(x_mm: float, y_mm: float) -> str:
    return frame_packet(f"OFFSET,{format_mm(x_mm)},{format_mm(y_mm)}")


def build_fire(
    seq: int, mm_x: float, mm_y: float, dwell_ms: int, power_permille: int
) -> str:
    payload = (
        f"FIRE,{int(seq)},"
        f"{format_mm(mm_x)},{format_mm(mm_y)},"
        f"{int(dwell_ms)},{int(power_permille)}"
    )
    return frame_packet(payload)


class SerialManager:
    """Best-effort serial transport with reconnect + DRY_RUN logging.

    The manager does not interpret packet contents. Callers pre-frame lines
    with `frame_packet(...)` (or the `build_*` helpers) and hand the final
    `$...*CS\\n` string to `send_line`.
    """

    def __init__(
        self,
        logger,
        port: str,
        baudrate: int,
        read_timeout_s: float,
        reconnect_s: float,
        dry_run: bool,
    ) -> None:
        self._log = logger
        self._port = port
        self._baudrate = baudrate
        self._read_timeout_s = read_timeout_s
        self._reconnect_s = reconnect_s
        self._dry_run = dry_run
        self._serial = None
        self._next_retry_at = 0.0
        self._warned_no_pyserial = False
        self._rx_buffer = ""

    @property
    def dry_run(self) -> bool:
        return self._dry_run

    @property
    def connected(self) -> bool:
        if self._dry_run:
            return True
        return bool(self._serial and self._serial.is_open)

    def ensure_connected(self) -> bool:
        if self._dry_run or self.connected:
            return True

        if serial is None:
            if not self._warned_no_pyserial:
                self._log.error("pyserial not installed. Run: pip install pyserial")
                self._warned_no_pyserial = True
            return False

        now = time.monotonic()
        if now < self._next_retry_at:
            return False
        self._next_retry_at = now + self._reconnect_s

        try:
            self._serial = serial.Serial(
                port=self._port,
                baudrate=self._baudrate,
                timeout=self._read_timeout_s,
                write_timeout=self._read_timeout_s,
            )
            self._log.info(f"Serial connected on {self._port} @ {self._baudrate}")
            return True
        except SerialException as exc:
            self._log.warn(f"Serial connect failed on {self._port}: {exc}")
            self._serial = None
            return False

    def send_line(self, line: str) -> bool:
        """Send one already-framed protocol line ending in '\\n'."""
        stripped = line.rstrip("\n")
        if self._dry_run:
            self._log.info(f"[DRY_RUN] would send: {stripped}")
            return True

        self._log.info(f"TX: {stripped}")
        if not self.ensure_connected():
            return False
        try:
            assert self._serial is not None
            self._serial.write(line.encode("ascii"))
            self._serial.flush()
            return True
        except (SerialException, OSError) as exc:
            self._log.error(f"Serial write failed: {exc}")
            self.close()
            return False

    def read_lines(self, limit: int = 32) -> List[str]:
        """Return up to `limit` newline-terminated lines received since last call."""
        lines: List[str] = []
        if self._dry_run or not self.connected:
            return lines
        assert self._serial is not None
        try:
            pending = self._serial.in_waiting
        except (SerialException, OSError) as exc:
            self._log.error(f"Serial read failed: {exc}")
            self.close()
            return lines
        if pending <= 0:
            return lines
        try:
            chunk = self._serial.read(pending)
        except (SerialException, OSError) as exc:
            self._log.error(f"Serial read failed: {exc}")
            self.close()
            return lines

        self._rx_buffer += chunk.decode("ascii", errors="ignore")
        while "\n" in self._rx_buffer and len(lines) < limit:
            line, self._rx_buffer = self._rx_buffer.split("\n", 1)
            line = line.strip("\r").strip()
            if line:
                lines.append(line)
        return lines

    def send_line_blocking_sync(self, line: str) -> bool:
        """Send a line, best effort, without requiring a prior ensure_connected.

        Used by shutdown paths where we want to push `$ARM,0` even if the
        regular poll loop has been torn down.
        """
        return self.send_line(line)

    def close(self) -> None:
        if self._serial is None:
            return
        try:
            self._serial.close()
        except Exception:  # pragma: no cover - defensive cleanup
            pass
        self._serial = None


__all__ = [
    "SerialManager",
    "build_arm",
    "build_fire",
    "build_offset",
    "frame_packet",
    "format_mm",
    "xor_checksum",
]
