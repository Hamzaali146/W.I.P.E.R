# test_model.py
from ultralytics import YOLO
import cv2

# Load your model
model = YOLO("/home/fatima/W.I.P.E.R/models/weights.pt")

# Open camera
cap = cv2.VideoCapture("http://192.168.18.9:8080/video")

if not cap.isOpened():
    print("Camera not opening")
    exit()

print("Camera connected")
print("Model loaded")
print("Running detection... press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print(" Frame read failed")
        continue

    # Run YOLO
    results = model(frame, verbose=False)

    # Draw boxes on frame
    annotated = results[0].plot()

    # Print detections in terminal
    boxes = results[0].boxes
    if boxes and len(boxes) > 0:
        print(f"Detected {len(boxes)} object(s):")
        for i, box in enumerate(boxes):
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            print(f"   [{i+1}] class={cls}, confidence={conf:.2f}")
    else:
        print("No weeds detected in this frame")

    # Show live video with boxes
    cv2.imshow("Weed Detection Test", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()