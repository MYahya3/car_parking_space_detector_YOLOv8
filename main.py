import cv2


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