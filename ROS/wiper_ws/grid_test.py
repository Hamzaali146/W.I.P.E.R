#!/usr/bin/env python3
"""Grid test for galvo calibration verification."""
import serial
import time

PORT = "/dev/ttyUSB0"
BAUD = 115200

def cs(payload: str) -> str:
    x = 0
    for c in payload:
        x ^= ord(c)
    return f"{x:02X}"

def send(ser, payload: str, wait_for_ack: bool = True):
    packet = f"${payload}*{cs(payload)}\r\n"
    print(f"TX: {packet.strip()}")
    ser.write(packet.encode())
    deadline = time.time() + 6.0
    while time.time() < deadline:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue
        print(f"RX: {line}")
        if line.startswith("ACK") or line.startswith("ERR") or line.startswith("INFO"):
            if wait_for_ack:
                return line
    if wait_for_ack:
        print("(no reply within timeout)")
    return None

def main():
    print(f"Opening {PORT} @ {BAUD}")
    ser = serial.Serial(PORT, BAUD, timeout=0.3)
    time.sleep(0.5)
    ser.reset_input_buffer()

    while ser.in_waiting:
        line = ser.readline().decode(errors="ignore").strip()
        if line:
            print(f"RX: {line}")

    send(ser, "ARM,1")
    time.sleep(0.3)

    send(ser, "FIRE,1,0,0,3000,750")
    input("\nCenter mark fired. Mark this dot as CENTER on cardboard.\nPress Enter to continue with grid...\n")

    grid = [
        ("FIRE,10,-100,-100,3000,750", "(-100, -100) back-right diagonal"),
        ("FIRE,11,0,-100,3000,750",     "(0, -100) straight back"),
        ("FIRE,12,100,-100,3000,750",   "(+100, -100) back-left diagonal"),
        ("FIRE,13,-100,0,3000,750",     "(-100, 0) right of center"),
        ("FIRE,14,0,0,3000,750",        "(0, 0) center repeat"),
        ("FIRE,15,100,0,3000,750",      "(+100, 0) left of center"),
        ("FIRE,16,-100,100,3000,750",   "(-100, +100) forward-right"),
        ("FIRE,17,0,100,3000,750",      "(0, +100) straight forward"),
        ("FIRE,18,100,100,3000,750",    "(+100, +100) forward-left"),
    ]
    for cmd, label in grid:
        print(f"\n>>> {label}")
        send(ser, cmd)
        time.sleep(0.3)

    send(ser, "HOME")
    send(ser, "ARM,0")
    ser.close()
    print("\nDone. Measure each dot from CENTER with a ruler.")
    print("Report back: direction and distance for each of points 10-18.")

if __name__ == "__main__":
    main()
