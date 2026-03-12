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

# import cv2
# from ultralytics import YOLO

# # 1. Load Your Custom Model
# # Make sure 'weights.pt' is in the same folder as this script
# model = YOLO('weights.pt')

# # 2. Define Your Camera Source
# # 'source=0' is typically your default webcam.
# # If you have multiple cameras, you can try 'source=1', 'source=2', etc.
# # You can also use a video file path: 'source="my_video.mp4"'
# results = model.predict(source=0, show=True, conf=0.5, stream=True)

# # 3. Process the Results
# # This loop will run until you close the display window
# try:
#     for r in results:
#         # model.predict() handles the drawing and displaying
#         # when 'show=True' is set.
#         # The 'r' object still contains all the data if you
#         # want to do custom processing (e.g., r.boxes, r.masks)
        
#         # We just need to keep the loop running
#         pass
        
# except KeyboardInterrupt:
#     # Handle user interruption (e.g., pressing Ctrl+C)
#     print("Stopping inference...")
# finally:
#     # Clean up
#     cv2.destroyAllWindows()
#     print("Inference stopped and windows closed.")
    
import cv2
from ultralytics import YOLO, solutions

# 1. Load your custom weed model
model = YOLO("weights.pt")

# 2. Setup Video Capture (0 for webcam)
cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error reading video stream"

# Get video dimensions for the display
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, 
                                        cv2.CAP_PROP_FRAME_HEIGHT, 
                                        cv2.CAP_PROP_FPS))

# 3. Initialize the Object Counter
# We use a simple line or region. If an object crosses it, it's counted.
# To count everything in the whole frame, we can define a large region.
region_points = [(0, 0), (w, 0), (w, h), (0, h)] # Full screen region

counter = solutions.ObjectCounter(
    show=True,              # Directly display the output window
    region=region_points,   # The area where counting happens
    model="weights.pt",     # Path to your weights
)

print("Starting weed counting... Press 'q' to stop.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    # The counter handles tracking and counting internally
    # It returns the annotated frame (im0)
    frame = counter.count_objects(frame)

    # Note: 'show=True' in ObjectCounter handles cv2.imshow for you.
    # We just need to check for the exit key 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()