

# To make detections and get required outputs
def YOLO_Detection(model, frame, conf=0.35):
    # Perform inference on an image
    results = model.predict(frame, conf=conf, classes = [0,2])
    # Extract bounding boxes, classes, names, and confidences
    boxes = results[0].boxes.xyxy.tolist()
    classes = results[0].boxes.cls.tolist()
    names = results[0].names
    return boxes, classes, names