#!/usr/bin/env python3
"""
FastAPI Backend for Weedbot Vision System
Provides REST API endpoints to interact with ROS 2 vision system
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import asyncio
import json
import cv2
from datetime import datetime
import threading
import time
from collections import deque

# ROS 2 imports
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from weedbot_interfaces.msg import WeedArray

# Initialize FastAPI
app = FastAPI(
    title="Weedbot Vision API",
    description="REST API for weedbot vision and laser control system",
    version="1.0.0"
)

# CORS middleware for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables
ros_bridge = None
ros_thread = None
fastapi_loop = None
active_websockets = []


# ==================== Pydantic Models ====================

class WeedDetectionResponse(BaseModel):
    """Single weed detection"""
    id: int
    confidence: float
    class_id: int
    bbox_x: float
    bbox_y: float
    bbox_w: float
    bbox_h: float
    real_world_x: float
    real_world_y: float
    real_world_z: float
    timestamp: str


class WeedArrayResponse(BaseModel):
    """Array of weed detections"""
    total_weeds: int
    detections: List[WeedDetectionResponse]
    inference_time_ms: float
    timestamp: str


class SystemStatus(BaseModel):
    """System status information"""
    camera_active: bool
    vision_active: bool
    laser_active: bool
    total_detections: int
    uptime_seconds: float
    last_detection_time: Optional[str]


class CameraSettings(BaseModel):
    """Camera configuration"""
    source: str
    frame_rate: float
    resolution_width: int
    resolution_height: int


class LaserCommand(BaseModel):
    """Laser firing command"""
    x_position: float  # meters
    y_position: float  # meters
    duration_ms: int   # milliseconds
    power_percent: float  # 0-100


# ==================== ROS 2 Bridge Node ====================

class ROSBridge(Node):
    """Bridge between ROS 2 and FastAPI"""
    
    def __init__(self):
        super().__init__('fastapi_ros_bridge')
        
        self.bridge = CvBridge()
        self.state_lock = threading.Lock()
        self.latest_image = None
        self.latest_viz_image = None
        self.latest_detections = None
        self.detection_history = deque(maxlen=200)
        self.total_detections = 0
        self.last_detection_time = None
        self.start_time = datetime.now()
        self.last_broadcast_time = 0.0
        self.broadcast_interval_sec = 0.1
        
        # Subscribers
        self.image_sub = self.create_subscription(
            Image,
            '/camera/image_raw',
            self.image_callback,
            10
        )
        
        self.viz_sub = self.create_subscription(
            Image,
            '/weedbot/visualization',
            self.viz_callback,
            10
        )
        
        self.detection_sub = self.create_subscription(
            WeedArray,
            '/weedbot/detections',
            self.detection_callback,
            10
        )
        
        # Publishers
        self.laser_pub = self.create_publisher(
            String,
            '/weedbot/laser_command',
            10
        )
        
        self.get_logger().info("ROS Bridge initialized")
    
    def image_callback(self, msg):
        """Store latest raw camera image"""
        try:
            image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            with self.state_lock:
                self.latest_image = image
        except Exception as e:
            self.get_logger().error(f"Image conversion error: {e}")
    
    def viz_callback(self, msg):
        """Store latest visualization image"""
        try:
            image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            with self.state_lock:
                self.latest_viz_image = image
        except Exception as e:
            self.get_logger().error(f"Viz conversion error: {e}")
    
    def detection_callback(self, msg):
        """Process weed detections"""
        timestamp = datetime.now().isoformat()
        detection_data = {
            'type': 'detection',
            'timestamp': timestamp,
            'total_weeds': int(msg.total_weeds),
            'inference_time_ms': float(msg.inference_time_ms),
            'detections': []
        }
        
        for i, det in enumerate(msg.detections):
            bbox_x = float(det.bbox_x[0]) if det.bbox_x else 0.0
            bbox_y = float(det.bbox_y[0]) if det.bbox_y else 0.0
            bbox_w = float(det.bbox_w[0]) if det.bbox_w else 0.0
            bbox_h = float(det.bbox_h[0]) if det.bbox_h else 0.0
            detection_data['detections'].append({
                'id': i,
                'confidence': float(det.confidences[0]) if det.confidences else 0.0,
                'class_id': int(det.class_ids[0]) if det.class_ids else 0,
                'bbox_x': bbox_x,
                'bbox_y': bbox_y,
                'bbox_w': bbox_w,
                'bbox_h': bbox_h,
                'center_x': bbox_x + (bbox_w / 2.0),
                'center_y': bbox_y + (bbox_h / 2.0),
                'real_world_x': float(det.real_world_x),
                'real_world_y': float(det.real_world_y),
                'real_world_z': float(det.real_world_z)
            })
        
        with self.state_lock:
            self.latest_detections = msg
            self.total_detections += int(msg.total_weeds)
            self.last_detection_time = timestamp
            self.detection_history.append(detection_data)

        # Bridge ROS thread -> FastAPI event loop safely
        now = time.monotonic()
        if now - self.last_broadcast_time < self.broadcast_interval_sec:
            return
        self.last_broadcast_time = now

        if fastapi_loop and fastapi_loop.is_running() and active_websockets:
            asyncio.run_coroutine_threadsafe(
                self.broadcast_detection(detection_data),
                fastapi_loop
            )
    
    async def broadcast_detection(self, data):
        """Send detection to all connected WebSocket clients"""
        disconnected = []
        for ws in list(active_websockets):
            try:
                await ws.send_json(data)
            except Exception:
                disconnected.append(ws)
        
        # Remove disconnected clients
        for ws in disconnected:
            if ws in active_websockets:
                active_websockets.remove(ws)
    
    def get_latest_image_bytes(self, use_visualization=True):
        """Get latest image as JPEG bytes"""
        with self.state_lock:
            if use_visualization:
                img = self.latest_viz_image if self.latest_viz_image is not None else self.latest_image
            else:
                img = self.latest_image if self.latest_image is not None else self.latest_viz_image

        if img is None:
            return None
        
        # Encode as JPEG
        success, buffer = cv2.imencode('.jpg', img)
        if not success:
            return None
        return buffer.tobytes()
    
    def fire_laser(self, x: float, y: float, duration_ms: int, power: float):
        """Send laser firing command"""
        command = {
            'action': 'fire',
            'x': x,
            'y': y,
            'duration_ms': duration_ms,
            'power_percent': power,
            'timestamp': datetime.now().isoformat()
        }
        
        msg = String()
        msg.data = json.dumps(command)
        self.laser_pub.publish(msg)
        
        self.get_logger().info(f"Laser command sent: {command}")


# ==================== ROS 2 Background Thread ====================

def ros_spin_thread():
    """Run ROS 2 in background thread"""
    global ros_bridge
    
    if not rclpy.ok():
        rclpy.init()
    ros_bridge = ROSBridge()
    
    try:
        rclpy.spin(ros_bridge)
    except KeyboardInterrupt:
        pass
    finally:
        if ros_bridge is not None:
            ros_bridge.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


# ==================== FastAPI Startup/Shutdown ====================

@app.on_event("startup")
async def startup_event():
    """Initialize ROS 2 bridge on startup"""
    global ros_thread, fastapi_loop

    fastapi_loop = asyncio.get_running_loop()
    ros_thread = threading.Thread(target=ros_spin_thread, daemon=True, name="ros2-spin")
    ros_thread.start()
    await asyncio.sleep(2)  # Give ROS time to initialize


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""
    global fastapi_loop
    fastapi_loop = None

    # Close any connected websocket clients
    for ws in list(active_websockets):
        try:
            await ws.close()
        except Exception:
            pass
    active_websockets.clear()

    if rclpy.ok():
        rclpy.shutdown()


# ==================== REST API Endpoints ====================

@app.get("/")
async def root():
    """API root endpoint"""
    return {
        "message": "Weedbot Vision API",
        "version": "1.0.0",
        "status": "operational",
        "endpoints": {
            "detections_latest": "/api/detections/latest",
            "detections_history": "/api/detections/history",
            "video_feed": "/api/video/stream",
            "system_status": "/api/system/status",
            "laser_fire": "/api/laser/fire"
        }
    }


@app.get("/api/detections/latest", response_model=WeedArrayResponse)
async def get_latest_detections():
    """Get latest weed detections"""
    if not ros_bridge:
        raise HTTPException(status_code=503, detail="ROS bridge not initialized")

    with ros_bridge.state_lock:
        msg = ros_bridge.latest_detections

    if msg is None:
        raise HTTPException(status_code=404, detail="No detections available")
    
    detections = []
    for i, det in enumerate(msg.detections):
        detections.append(WeedDetectionResponse(
            id=i,
            confidence=det.confidences[0] if det.confidences else 0.0,
            class_id=det.class_ids[0] if det.class_ids else 0,
            bbox_x=det.bbox_x[0] if det.bbox_x else 0.0,
            bbox_y=det.bbox_y[0] if det.bbox_y else 0.0,
            bbox_w=det.bbox_w[0] if det.bbox_w else 0.0,
            bbox_h=det.bbox_h[0] if det.bbox_h else 0.0,
            real_world_x=det.real_world_x,
            real_world_y=det.real_world_y,
            real_world_z=det.real_world_z,
            timestamp=datetime.now().isoformat()
        ))
    
    return WeedArrayResponse(
        total_weeds=msg.total_weeds,
        detections=detections,
        inference_time_ms=msg.inference_time_ms,
        timestamp=datetime.now().isoformat()
    )


@app.get("/api/detections/history")
async def get_detection_history(limit: int = 50):
    """Get detection history"""
    if not ros_bridge:
        raise HTTPException(status_code=503, detail="ROS bridge not initialized")

    limit = max(1, min(limit, 500))
    with ros_bridge.state_lock:
        full_history = list(ros_bridge.detection_history)
        history = full_history[-limit:]
    
    return {
        "total_records": len(full_history),
        "history": history
    }


@app.get("/api/system/status", response_model=SystemStatus)
async def get_system_status():
    """Get system status"""
    if not ros_bridge:
        raise HTTPException(status_code=503, detail="ROS bridge not initialized")
    
    uptime = (datetime.now() - ros_bridge.start_time).total_seconds()
    with ros_bridge.state_lock:
        camera_active = ros_bridge.latest_image is not None
        vision_active = ros_bridge.latest_viz_image is not None or ros_bridge.latest_image is not None
        total_detections = ros_bridge.total_detections
        last_detection = ros_bridge.last_detection_time
    
    return SystemStatus(
        camera_active=camera_active,
        vision_active=vision_active,
        laser_active=True,  # TODO: Add actual laser status
        total_detections=total_detections,
        uptime_seconds=uptime,
        last_detection_time=last_detection
    )


@app.get("/api/video/stream")
async def video_stream():
    """Stream video feed as MJPEG"""
    
    async def generate_frames():
        while True:
            if ros_bridge:
                frame_bytes = ros_bridge.get_latest_image_bytes(use_visualization=True)
                
                if frame_bytes:
                    yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            
            await asyncio.sleep(0.033)  # ~30 FPS
    
    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


@app.get("/api/video/snapshot")
async def get_snapshot():
    """Get single frame snapshot"""
    if not ros_bridge:
        raise HTTPException(status_code=503, detail="ROS bridge not initialized")

    frame_bytes = ros_bridge.get_latest_image_bytes(use_visualization=True)
    if frame_bytes is None:
        raise HTTPException(status_code=404, detail="No image available")
    
    return StreamingResponse(
        iter([frame_bytes]),
        media_type="image/jpeg"
    )


@app.post("/api/laser/fire")
async def fire_laser(command: LaserCommand):
    """Fire laser at specified position"""
    if not ros_bridge:
        raise HTTPException(status_code=503, detail="ROS bridge not initialized")
    
    # Validate parameters
    if not (-2.0 <= command.x_position <= 2.0):
        raise HTTPException(status_code=400, detail="X position out of range (-2 to 2 meters)")
    
    if not (-2.0 <= command.y_position <= 2.0):
        raise HTTPException(status_code=400, detail="Y position out of range (-2 to 2 meters)")
    
    if not (0 < command.power_percent <= 100):
        raise HTTPException(status_code=400, detail="Power must be between 0 and 100")
    
    # Send command
    ros_bridge.fire_laser(
        command.x_position,
        command.y_position,
        command.duration_ms,
        command.power_percent
    )
    
    return {
        "status": "success",
        "message": "Laser command sent",
        "command": command.dict()
    }


@app.post("/api/laser/fire-at-weed/{weed_id}")
async def fire_laser_at_weed(weed_id: int):
    """Fire laser at detected weed by ID"""
    if not ros_bridge:
        raise HTTPException(status_code=503, detail="ROS bridge not initialized")

    with ros_bridge.state_lock:
        latest_detections = ros_bridge.latest_detections

    if latest_detections is None:
        raise HTTPException(status_code=404, detail="No detections available")
    
    detections = latest_detections.detections
    
    if weed_id >= len(detections):
        raise HTTPException(status_code=404, detail="Weed ID not found")
    
    weed = detections[weed_id]
    
    # Fire laser at weed position
    ros_bridge.fire_laser(
        weed.real_world_x,
        weed.real_world_y,
        duration_ms=100,
        power=80.0
    )
    
    return {
        "status": "success",
        "message": f"Laser fired at weed {weed_id}",
        "position": {
            "x": weed.real_world_x,
            "y": weed.real_world_y
        }
    }


# ==================== WebSocket Endpoint ====================

@app.websocket("/ws/detections")
async def websocket_detections(websocket: WebSocket):
    """WebSocket for real-time detection streaming"""
    await websocket.accept()
    active_websockets.append(websocket)
    
    try:
        while True:
            # Keep connection alive
            await asyncio.sleep(10)
            await websocket.send_json({"type": "ping", "timestamp": datetime.now().isoformat()})
            
    except WebSocketDisconnect:
        pass
    finally:
        if websocket in active_websockets:
            active_websockets.remove(websocket)


# ==================== Statistics Endpoints ====================

@app.get("/api/stats/summary")
async def get_statistics():
    """Get detection statistics"""
    if not ros_bridge:
        raise HTTPException(status_code=503, detail="ROS bridge not initialized")
    
    with ros_bridge.state_lock:
        total_frames = len(ros_bridge.detection_history)
        total_weeds = ros_bridge.total_detections
    avg_weeds_per_frame = total_weeds / total_frames if total_frames > 0 else 0
    
    return {
        "total_frames_processed": total_frames,
        "total_weeds_detected": total_weeds,
        "average_weeds_per_frame": round(avg_weeds_per_frame, 2),
        "uptime_seconds": (datetime.now() - ros_bridge.start_time).total_seconds()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
