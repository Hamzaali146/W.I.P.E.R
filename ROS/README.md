# Weedbot — Laser Weeding Robot (ROS 2)

An autonomous laser weeding system built on ROS 2. It uses a YOLO model for real-time weed detection, homography to map detections into real-world ground coordinates, and a laser galvo system to fire precisely at each weed.

---

## System Architecture

```
IP Camera
    │
    ▼ /camera/image_raw (30 Hz)
camera_publisher
    │
    ▼ /camera/image_raw
vision_node  ──────────────────────────────────────────────────►  /weedbot/visualization
    │  (YOLOv8 + homography)
    ▼ /weedbot/detections (WeedArray)
    ├──► control_node  ──► Serial ($SHOT packets) ──► STM32 ──► Galvo + Laser
    ├──► detection_monitor  (statistics)
    └──► FastAPI bridge  ──► REST / WebSocket / MJPEG stream
```

---

## Packages

| Package | Description |
|---|---|
| `weedbot_interfaces` | Custom ROS 2 message definitions (`WeedDetection`, `WeedArray`) |
| `weedbot_vision` | Camera publisher, YOLO detection node, homography calibration |
| `weedbot_control` | Laser galvo control, serial communication with STM32 |
| `weedbot_simulation` | Gazebo simulation (tractor, weed spawner, simulated laser) |
| `weedbot_api` | FastAPI REST and WebSocket server for monitoring and control |

---

## Message Definitions

### `WeedDetection.msg` — one detected weed

```
std_msgs/Header header

float32[] bbox_x        # Bounding box left edge, normalized 0–1
float32[] bbox_y        # Bounding box top edge, normalized 0–1
float32[] bbox_w        # Bounding box width, normalized 0–1
float32[] bbox_h        # Bounding box height, normalized 0–1
float32[] confidences   # YOLO confidence scores
int32[]   class_ids     # 0 = Weed

float32 real_world_x    # Lateral position in meters (+right, -left)
float32 real_world_y    # Forward position in meters (+forward, -backward)
float32 real_world_z    # Always 0.0 (ground plane)

sensor_msgs/Image mask  # Optional segmentation mask
```

### `WeedArray.msg` — one frame's detections

```
std_msgs/Header header
WeedDetection[] detections    # All weeds detected this frame
int32           total_weeds
float64         inference_time_ms
```

---

## Topics

| Topic | Type | Direction | Description |
|---|---|---|---|
| `/camera/image_raw` | `sensor_msgs/Image` | camera → vision | Raw camera frames at 30 Hz |
| `/weedbot/detections` | `WeedArray` | vision → control/monitor/API | Per-frame weed detections with real-world coords |
| `/weedbot/visualization` | `sensor_msgs/Image` | vision → API | Annotated frames with bounding boxes |
| `/weedbot/laser_command` | `std_msgs/String` (JSON) | API → control | Manual laser fire commands |
| `/weedbot/control/status` | `std_msgs/String` (JSON) | control → API | System status at 1 Hz |
| `/weedbot/control/debug` | `std_msgs/String` (JSON) | control → API | Per-shot telemetry (angles, voltages, DAC codes) |

---

## Nodes

### `camera_publisher`
- **Input:** IP camera stream (`https://192.168.100.249:8080/video`) or USB (`/dev/video0`)
- **Output:** `/camera/image_raw` at 30 Hz
- Auto-reconnects on drop. Supports horizontal/vertical flip.

### `vision_node`
- **Input:** `/camera/image_raw`
- **Output:** `/weedbot/detections`, `/weedbot/visualization`
- Runs YOLOv8 instance segmentation (`models/weights.pt`)
- Filters to class 0 (Weed) only
- Transforms bounding box centers to real-world meters via homography matrix
- Key parameters:
  - `confidence_threshold: 0.15`
  - `iou_threshold: 0.4`
  - `input_size: 640`
  - `device: cpu` (or `cuda`)

### `camera_calibration`
- **Input:** `/camera/image_raw`
- **Output:** `config/homography_matrix.yaml`
- Interactive OpenCV tool. Click 4 ground-plane points, enter real-world (X, Y) meters per point.
- Computes and saves the 3×3 homography matrix.

### `detection_monitor`
- **Input:** `/weedbot/detections`
- Logs statistics every 5 seconds: frames processed, total detections, avg detections/frame, avg confidence, avg inference time.

### `control_node`
- **Input:** `/weedbot/detections`
- **Output:** `/weedbot/control/status`, `/weedbot/control/debug`, serial port
- Takes the detection meristem (bbox center in real-world meters from homography), converts to firmware-frame millimeters, and emits `$FIRE,<seq>,<mm_x>,<mm_y>,<dwell_ms>,<power_permille>*CS`
- Safety interlocks: `mode` (DRY_RUN vs LIVE), `armed` flag, confidence gate, cooldown, deduplication, reachable-envelope bounds (offset-aware), 14-shot outstanding-queue cap
- On LIVE startup: sends `$ARM,1` then `$OFFSET,x,y`. On shutdown (SIGINT/SIGTERM/ROS teardown): sends `$ARM,0` — the firmware watchdog is currently disabled, so this disarm is required to keep the laser safe.

### `laser_test_node`
- **Output:** `/weedbot/detections` (fake `WeedArray`, one detection per tick)
- Replays `config/test_shots.csv` so you can exercise the control node without the camera. Use with `laser_dry_run.launch.py`.

---

## Detection → Laser Shot Pipeline

```
WeedDetection received
        │
        ├─ confidence >= min_confidence?               (else skip)
        ├─ duplicate suppression:
        │    same mm target within duplicate_radius_mm
        │    AND within duplicate_holdoff_ms?          (else skip)
        └─ cooldown: shot_cooldown_ms since last?      (else skip)
                │
         best target selected (highest_confidence | nearest_center)
                │
         meristem = bbox center → real_world_x/y (meters, from homography)
                │
         meters → mm   (× 1000)
                │
         sign flip into firmware frame
           sign_flip_x: vision +right  → firmware +left
           sign_flip_y: vision +toward → firmware +forward
                │
         bounds check (offset-aware):
           reachable = target_mm − cam_to_galvo_offset_mm
           reject if outside [bounds_*_min_mm, bounds_*_max_mm]
                │
         queue check: outstanding shots < queue_max_outstanding (14)
                │
         serial packet:
           $FIRE,<seq>,<mm_x>,<mm_y>,<dwell_ms>,<power_permille>*<CS>
           e.g.  $FIRE,17,37.5,-12.0,500,750*7A
                │
         STM32 replies (after shot completes): ACK,<seq> or ERR,<seq>,<reason>
```

On startup (`mode: LIVE` and `armed: true`) the control node sends
`$ARM,1` followed by `$OFFSET,<x>,<y>` with the camera-to-galvo offset
parameters, pushing the offset into firmware so both sides agree.

---

## Homography

The homography matrix maps any pixel coordinate in the camera image to a real-world position (in meters) on the flat ground plane.

**Origin:** camera center projected vertically onto the ground  
**Axes:** +X = right, +Y = forward (robot frame)

### Calibration

```bash
ros2 launch weedbot_vision calibration.launch.py
```

1. An OpenCV window shows the live camera feed.
2. Click 4 points on the ground plane (corners of a known reference area).
3. Enter the real-world (X, Y) in meters for each point.
4. The matrix is computed and saved to `src/weedbot_vision/config/homography_matrix.yaml`.

### Runtime transformation

```python
pixel_point = np.array([[[center_x_px, center_y_px]]], dtype=np.float32)
real_point  = cv2.perspectiveTransform(pixel_point, H)
# → real_world_x (m), real_world_y (m)
```

---

## Coordinate Systems

```
Pixel coords          (0,0 top-left, camera native resolution)
  → Normalized        (0.0–1.0, stored in bbox_x/y/w/h)
    → Real-world      (meters, via 3×3 homography; +x right, +y toward operator)
      → Millimeters   (× 1000)
        → Firmware frame  (+mm_x = LEFT, +mm_y = FORWARD)
          → Bounds-checked against reachable envelope (±250 mm default)
            → $FIRE packet → STM32 → galvo + laser
```

---

## Serial Protocol

All packets are ASCII, terminated by `\n`, `CS` = XOR of payload bytes (everything between `$` and `*`) rendered as 2-char uppercase hex.

**Frame format:** `$<payload>*<CS>\n`

| Packet | Direction | Format | Example |
|---|---|---|---|
| Arm / Disarm | PC → MCU | `$ARM,<0\|1>*<CS>` | `$ARM,1*F3` |
| Offset | PC → MCU | `$OFFSET,<x_mm>,<y_mm>*<CS>` | `$OFFSET,0.0,0.0*XX` |
| Fire | PC → MCU | `$FIRE,<seq>,<mm_x>,<mm_y>,<dwell_ms>,<power_permille>*<CS>` | `$FIRE,17,37.5,-12.0,500,750*7A` |
| Ack | MCU → PC | `ACK,<seq>` | `ACK,17` |
| Error | MCU → PC | `ERR,<seq>,<reason>` | `ERR,17,DISARMED` |
| Boot | MCU → PC | `BOOT,READY` | |

**Error reasons:** `DISARMED`, `OUT_OF_RANGE`, `QUEUE_FULL`, `CS_MISMATCH`, `SHOT_ARG_FMT`

Notes:
- `mm_x`, `mm_y` are signed floats in millimeters, formatted with `.1f` (e.g. `0.0`, `-37.5`).
- `dwell_ms` is an unsigned integer in `[0, 5000]`.
- `power_permille` is an unsigned integer in `[0, 1000]` (e.g. `750` = 75% power).
- The firmware handles galvo settle (~12 ms) internally — not a packet field.
- ACK arrives **after** the shot completes (galvo move + dwell), not at enqueue. Use `ack_timeout_ms ≥ 10000`.
- Firmware has a 16-shot internal queue; send at most 14 outstanding shots to stay clear of `QUEUE_FULL`.

---

## Key Configuration

### Vision — `src/weedbot_vision/config/vision_params.yaml`

```yaml
/weedbot_vision_node:
  model_path: '.../models/weights.pt'
  confidence_threshold: 0.15
  iou_threshold: 0.4
  input_size: 640
  device: 'cpu'
  publish_viz: true

/camera_publisher:
  camera_source: "https://192.168.100.249:8080/video"
  frame_rate: 30.0
  flip_horizontal: true
  flip_vertical: true
```

### Control — `src/weedbot_control/config/control_params.yaml`

```yaml
/weedbot_control_node:
  mode: "DRY_RUN"                # or "LIVE"
  armed: false                   # MUST be true before any $FIRE is sent
  auto_fire_enabled: true

  min_confidence: 0.60
  target_policy: "highest_confidence"  # or "nearest_center"
  shot_cooldown_ms: 220.0
  duplicate_radius_mm: 15.0
  duplicate_holdoff_ms: 600.0

  dwell_ms: 500                  # 0..5000
  power_permille: 750            # 0..1000 (750 = 75%)

  sign_flip_x: true              # vision +right → firmware +left
  sign_flip_y: true              # vision +toward → firmware +forward
  cam_to_galvo_offset_x_mm: 0.0  # applied by firmware via $OFFSET
  cam_to_galvo_offset_y_mm: 0.0
  bounds_x_min_mm: -250.0        # reachable envelope (15 mm margin from ±265)
  bounds_x_max_mm:  250.0
  bounds_y_min_mm: -250.0
  bounds_y_max_mm:  250.0

  queue_max_outstanding: 14      # firmware queue is 16, leave headroom
  ack_timeout_ms: 10000          # ACK arrives AFTER shot completes

  serial_port: "/dev/ttyUSB0"
  serial_baudrate: 115200
  serial_read_timeout_s: 0.02
  serial_reconnect_s: 2.0
  serial_poll_hz: 50.0
```

---

## Launch

### Vision only
```bash
ros2 launch weedbot_vision vision_launch.py
```

### Homography calibration
```bash
ros2 launch weedbot_vision calibration.launch.py
```

### Control node — dry run (no hardware)
```bash
ros2 launch weedbot_control laser_dry_run.launch.py
# Launches control_node + laser_test_node. Every would-be $FIRE packet is
# logged at INFO with its full framed form including *CS. Copy one into
# TeraTerm on the STM32 laptop to verify the firmware accepts the format.
```

### Control node — live (STM32 connected)
```bash
ros2 launch weedbot_control laser_dry_run.launch.py \
  mode:=LIVE serial_port:=/dev/ttyUSB0 armed:=true
# On startup the node sends $ARM,1 then $OFFSET,x,y with the YAML offset
# values. On Ctrl+C it sends $ARM,0 before closing the serial port.
```

### Gazebo simulation
```bash
ros2 launch weedbot_simulation full_system_launch.py
```

### API server
```bash
cd src/weedbot_api
python3 main.py
# → http://localhost:8000
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API info |
| GET | `/api/detections/latest` | Latest detections (JSON) |
| GET | `/api/detections/history?limit=50` | Detection history |
| GET | `/api/system/status` | System status |
| GET | `/api/video/stream` | MJPEG live video |
| GET | `/api/video/snapshot` | Single JPEG frame |
| POST | `/api/laser/fire` | Fire laser at position |
| POST | `/api/laser/fire-at-weed/{weed_id}` | Fire at a detected weed |
| GET | `/api/stats/summary` | Detection statistics |
| WS | `/ws/detections` | Real-time detection stream |

**Example — fire laser:**
```bash
curl -X POST http://localhost:8000/api/laser/fire \
  -H "Content-Type: application/json" \
  -d '{"x_position": 0.3, "y_position": 1.2, "duration_ms": 90, "power_percent": 75.0}'
```

---

## Building

```bash
cd /home/hamza/wiper_ws

# Build interfaces first (other packages depend on it)
colcon build --packages-select weedbot_interfaces
source install/setup.bash

# Build the rest
colcon build --packages-select weedbot_vision weedbot_control weedbot_simulation
source install/setup.bash
```

---

## Dependencies

| Category | Libraries |
|---|---|
| ROS 2 | `rclpy`, `sensor_msgs`, `std_msgs`, `cv_bridge`, `gazebo_ros` |
| Vision | `ultralytics` (YOLOv8), `opencv-python`, `numpy`, `torch` |
| Control | `pyserial` |
| API | `fastapi`, `uvicorn`, `pydantic` |

---

## Safety Notes

- The system starts **disarmed** and in **dry-run mode** by default. No laser fires until you explicitly set `armed: true` and `dry_run: false`.
- Minimum confidence to fire: **0.60** (configurable).
- Cooldown between shots: **220 ms**.
- Duplicate suppression prevents re-firing at the same weed within **600 ms**.
- Galvo angles are hard-clamped to **±20°** in both axes.
- Optional real-world bounds gate: lateral ±0.80 m, forward 0.10–2.50 m.
