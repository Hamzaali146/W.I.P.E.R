# import cv2
# from ultralytics import YOLO

# model = YOLO('runs/detect/wheat_weed_yolov8s/weights/best.pt')  

# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("Error: Could not open webcam.")
#     exit()

# while True:

#     success, frame = cap.read()

#     if success:

#         results = model(frame, stream=True)

#         for r in results:
#             annotated_frame = r.plot()
            

#             cv2.imshow("YOLOv8 Webcam Inference", annotated_frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         print("Error: Could not read frame.")
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO

# 1. Load Your Custom Model
# Make sure 'weights.pt' is in the same folder as this script
model = YOLO('weights.pt')

# 2. Define Your Camera Source
# 'source=0' is typically your default webcam.
# If you have multiple cameras, you can try 'source=1', 'source=2', etc.
# You can also use a video file path: 'source="my_video.mp4"'
results = model.predict(source=0, show=True, conf=0.5, stream=True)

# 3. Process the Results
# This loop will run until you close the display window
try:
    for r in results:
        # model.predict() handles the drawing and displaying
        # when 'show=True' is set.
        # The 'r' object still contains all the data if you
        # want to do custom processing (e.g., r.boxes, r.masks)
        
        # We just need to keep the loop running
        pass
        
except KeyboardInterrupt:
    # Handle user interruption (e.g., pressing Ctrl+C)
    print("Stopping inference...")
finally:
    # Clean up
    cv2.destroyAllWindows()
    print("Inference stopped and windows closed.")
# import cv2
# import numpy as np
# from ultralytics import YOLO, solutions

# # 1. Load your model
# model = YOLO("weights.pt")

# # 2. Open the camera
# cap = cv2.VideoCapture(0)
# assert cap.isOpened(), "Error reading video stream"

# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # 3. Define a "Thin Rectangle" across the middle
# # We use 4 points to form a box. This prevents the 'NoneType' intersects error.
# # The box is 20 pixels tall (from h/2 - 10 to h/2 + 10)
# line_points = [(0, h // 2 - 10), (w, h // 2 - 10), (w, h // 2 + 10), (0, h // 2 + 10)] 

# # 4. Initialize the Object Counter
# counter = solutions.ObjectCounter(
#     show=True,
#     region=line_points,
#     model="weights.pt",
# )

# print("Starting weed counting... Press 'q' to stop.")

# try:
#     while cap.isOpened():
#         success, frame = cap.read()
#         if not success:
#             break

#         # 5. Run tracking (Using persist=True for counting)
#         # lowered conf to 0.3 to ensure it catches weeds
#         results = model.track(frame, persist=True, show=False, conf=0.3)

#         # 6. Safety check: Only run counter if detections exist
#         if results[0].boxes is not None and results[0].boxes.id is not None:
#             boxes = results[0].boxes.xyxy.cpu()
#             track_ids = results[0].boxes.id.int().cpu().tolist()
#             clss = results[0].boxes.cls.int().cpu().tolist()

#             try:
#                 # This updates the 'In' and 'Out' counts
#                 frame = counter.count_objects(frame, track_ids, boxes, clss)
#             except Exception as e:
#                 # If the counter still glitches, draw boxes manually so it doesn't crash
#                 for box, track_id in zip(boxes, track_ids):
#                     x1, y1, x2, y2 = map(int, box)
#                     cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
#                     cv2.putText(frame, f"ID:{track_id}", (x1, y1-10), 0, 0.6, (0, 255, 0), 2)
#         else:
#             # If no detections, just draw the counting zone manually
#             cv2.polylines(frame, [np.array(line_points, dtype=np.int32)], True, (0, 255, 255), 2)
#             cv2.putText(frame, "Status: Scanning...", (20, 40), 
#                         cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

#         # 7. Final display
#         cv2.imshow("WeedBot Counter", frame)

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

# except Exception as e:
#     print(f"Global Error: {e}")

# finally:
#     cap.release()
#     cv2.destroyAllWindows()
#     print("Inference stopped.")