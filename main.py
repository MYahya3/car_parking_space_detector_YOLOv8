import cv2
import torch
from utilis import YOLO_Detection
from ultralytics import YOLO


# Check if CUDA is available
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# Load YOLO model and move it to the appropriate device
model = YOLO("yolov8n.pt")
model.to(device)

# Capture from camera or video
cap = cv2.VideoCapture("parking_space.mp4")  # Change to the appropriate source if not using a webcam
# get vcap property
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float `width`
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Perform YOLO detection
    boxes, classes, names = YOLO_Detection(model, frame)

    # Collect points to determine if any detection is inside polygons
    detection_points = []
    for box in boxes:
        x1, y1, x2, y2 = box
        center_x = ((x1 + x2) / 2)
        center_y = ((y1 + y2) / 2)
        detection_points.append((int(center_x), int(center_y)))