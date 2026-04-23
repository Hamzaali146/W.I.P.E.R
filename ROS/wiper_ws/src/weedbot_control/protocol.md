# Serial Protocol and Mapping

## 1) Coordinate Mapping in Control Node

Given detection center in pixels `(px, py)` and image size `(W, H)`:

- `x_norm = (px / W) - 0.5`
- `y_norm = 0.5 - (py / H)`

Camera angles:

- `angle_x_deg = x_norm * camera_fov_x_deg`
- `angle_y_deg = y_norm * camera_fov_y_deg`

Then clamp to galvo limits:

- `[-galvo_x_max_deg, +galvo_x_max_deg]`
- `[-galvo_y_max_deg, +galvo_y_max_deg]`

Voltage mapping is piecewise linear around calibrated center:

- If `angle >= 0`:
  - `v = v_center + (angle / max_angle) * (v_max - v_center)`
- If `angle < 0`:
  - `v = v_center + (angle / max_angle) * (v_center - v_min)`

DAC code:

- `dac_code = round((v / dac_vref) * ((2^dac_bits)-1))`

## 2) Framing

Packets are one line:

- `$<payload>*<checksum>\n`

`checksum` = XOR of payload bytes (ASCII), encoded as 2 hex chars.

Example payload:

- `SHOT,17,32110,28790,12000,90000,750`

Example frame:

- `$SHOT,17,32110,28790,12000,90000,750*5C`

## 3) Commands

- `ARM,<state>`
  - `state=0` disarm
  - `state=1` arm

- `SHOT,<seq>,<dac_x>,<dac_y>,<settle_us>,<fire_us>,<power_permille>`
  - `seq`: rolling sequence number
  - `dac_x`, `dac_y`: 0..65535
  - `settle_us`: galvo settling wait before laser
  - `fire_us`: pulse width
  - `power_permille`: 0..1000

- `PING,<seq>`
  - link health check

## 4) Replies from STM32

- `ACK,<seq>`
- `ERR,<seq>,<reason>`

Common reasons:

- `DISARMED`
- `SHOT_RANGE`
- `CS_MISMATCH`
- `SHOT_ARG_FMT`

## 5) Recommended Runtime Limits

- `fire_us` <= `1000000` (1 second)
- `power_permille` <= `1000`
- keep `shot_cooldown_ms` high enough to avoid thermal runaway
- always use hardware interlocks independent of software
