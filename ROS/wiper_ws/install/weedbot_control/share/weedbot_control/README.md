# weedbot_control

Control stack for field hardware:

1. Subscribe to weed detections from vision (`/weedbot/detections`)
2. Convert weed center pixel -> galvo angles -> voltages -> DAC codes
3. Send shot packets over USB-TTL serial to STM32
4. STM32 writes DAC8563 and fires the laser pulse

## Safety First

- Keep `armed: false` until calibration and enclosure/interlock checks are complete.
- Run initial bring-up with `dry_run: true` so no real serial writes happen.
- Add hardware interlocks (key switch, E-stop, lid switch) outside software.

## ROS2 Node

- Node executable: `control_node`
- Launch file: `launch/control_launch.py`
- Default config: `config/control_params.yaml`

Main tune points:

- `camera_fov_x_deg`, `camera_fov_y_deg`: camera optics model
- `galvo_x_max_deg`, `galvo_y_max_deg`: allowed scan angle limits
- `x_min_voltage/x_center_voltage/x_max_voltage` and same for `y`: galvo amp calibration
- `min_confidence`, `shot_cooldown_ms`: weed targeting behavior
- `serial_port`, `serial_baudrate`: STM32 link

## Packet Protocol

Transport is ASCII line packets with checksum:

- Frame format: `$<payload>*<CS>\n`
- `CS`: XOR of payload bytes, uppercase hex

Commands sent by ROS:

- `ARM` packet: `ARM,<0|1>`
- `SHOT` packet:
  `SHOT,<seq>,<dac_x>,<dac_y>,<settle_us>,<fire_us>,<power_permille>`

STM32 replies:

- `ACK,<seq>`
- `ERR,<seq>,<reason>`

Full details: see [protocol.md](protocol.md).

## Bring-up

1. Build packages:

```bash
cd ROS/wiper_ws
colcon build --packages-select weedbot_interfaces weedbot_control
source install/setup.bash
```

2. Start in dry run:

```bash
ros2 launch weedbot_control control_launch.py dry_run:=true armed:=false
```

3. When serial and mapping are validated:

```bash
ros2 launch weedbot_control control_launch.py serial_port:=/dev/ttyUSB0 dry_run:=false armed:=false
```

4. Arm only after final checks:

```bash
ros2 param set /weedbot_control_node armed true
```

## Calibration Flow

1. Keep laser physically disabled (or power set to safe marker level).
2. Send targets at image corners/center, record actual spot location.
3. Tune:
   - camera FOV parameters for angle mapping
   - min/center/max voltage for each axis
4. Verify scan stays inside plant bed and never crosses forbidden zones.
5. Enable full pulse duration/power only after repeatability is stable.

## Firmware Reference

Reference STM32 implementation is in:

- [firmware/stm32_laser_controller_reference.c](firmware/stm32_laser_controller_reference.c)

It expects:

- `huart1` for USB-TTL command input
- `hspi1` for DAC8563
- `htim2` at 1 MHz for microsecond delays
- `htim3` PWM for laser power

Adjust GPIO and timer mappings for your board.
