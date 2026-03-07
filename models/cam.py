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