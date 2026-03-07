#!/usr/bin/env python3
from ultralytics import YOLO
import sys

model_path = '/home/hamza/wiper_ws/src/weedbot_vision/models/weights.pt'

print(f"Testing model: {model_path}")

try:
    model = YOLO(model_path)
    print("✓ Model loaded successfully!")
    print(f"Model type: {type(model)}")
    print(f"Model names: {model.names}")
except Exception as e:
    print(f"✗ Failed to load model: {e}")
    sys.exit(1)