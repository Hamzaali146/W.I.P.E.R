from ultralytics import YOLO
import numpy as np

class WeedDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def process_frame(self, frame):
        results = self.model(frame, verbose=False)

        detections = []
        h, w = frame.shape[:2]

        for result in results:
            boxes = result.boxes
            if boxes is None:
                continue

            for i in range(len(boxes)):
                box = boxes.xyxy[i].cpu().numpy()
                x1, y1, x2, y2 = box

                conf = float(boxes.conf[i].cpu().numpy())
                cls = int(boxes.cls[i].cpu().numpy())

                center_x = (x1 + x2) / 2 / w
                center_y = (y1 + y2) / 2 / h

                detections.append({
                    "bbox": [x1/w, y1/h, (x2-x1)/w, (y2-y1)/h],
                    "confidence": conf,
                    "class_id": cls,
                    "real_world_x": center_x,   # TEMP (you will replace later)
                    "real_world_y": center_y
                })

        return detections