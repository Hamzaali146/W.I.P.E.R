# weedbot_vision_service/vision_service.py
import zmq
import cv2
import json
import threading
import numpy as np
from fastapi import FastAPI
from detector import WeedDetector

app = FastAPI()

#Custom JSON encoder to handle NumPy types (float32, int64, ndarray)
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super().default(obj)

#ZMQ setup: this SENDS coordinates to bridge.py
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:5555")  # bridge.py is listening here

#YOLO model 
detector = WeedDetector("/home/fatima/W.I.P.E.R/models/weights.pt")

#Camera (your IP webcam)
cap = cv2.VideoCapture("http://192.168.18.9:8080/video")

is_running = False  # flag to start/stop loop

def detection_loop():
    global is_running

    # Check if camera opened
    if not cap.isOpened():
        print("Camera not opened in detection_loop!")
        is_running = False
        return

    print("Detection loop started")

    while is_running:
        ret, frame = cap.read()
        if not ret:
            print("Frame read failed")
            continue

        detections = detector.process_frame(frame)
        print(f"Detected {len(detections)} weeds")

        if len(detections) > 0:
            try:
                payload = json.dumps({"detections": detections}, cls=NumpyEncoder)
                socket.send_string(payload)
                print(f"Sent {len(detections)} detections to ROS bridge")
            except TypeError as e:
                print(f"Serialization error: {e}")

#API endpoints
@app.get("/")
def home():
    return {"status": "Vision Service Running", "active": is_running}

@app.get("/start")
def start():
    global is_running
    if not is_running:
        is_running = True
        threading.Thread(target=detection_loop, daemon=True).start()
        return {"status": "started"}
    return {"status": "already running"}

@app.get("/stop")
def stop():
    global is_running
    is_running = False
    return {"status": "stopped"}