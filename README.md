# Car_Parking_Space_Detector_YOLOv8

## Description

This project utilizes YOLOv8n (You Only Look Once) to detect objects in a Parking Space and determine the availability of parking spaces based on predefined polygons. The system highlights detected objects and counts the number of occupied and free parking slots.

## Input Parking Space Video :
 ![Screenshot (93)](https://github.com/user-attachments/assets/3aa2a1c8-ca29-4fbc-b623-dfcf5f52ba72)

## Output Resulted Parking Space

![Screenshot (94)](https://github.com/user-attachments/assets/4f48e9a2-5623-4b8a-bd09-d9991d75b11b)

## Prerequisites

- Python 3.7 or later

## Installation

1. **Clone the repository:**

    ```bash
    git clone <https://github.com/MYahya3/Car_Parking_Space_Detector_YOLOv8.git>
    cd <Car_Parking_Space_Detector_YOLOv8>
    ```

2. **Set Up a Virtual Environment (optional but recommended):**

    ```bash
    conda activate YOLO
    ```

3. **Install Dependencies:**

    Ensure you have the `requirements.txt` file in the project directory. Install the necessary Python packages with:

    ```bash
    pip install -r requirements.txt
    ```

4. **Download YOLOv8 Model:**

    Ensure you have the `yolov8n.pt` model file in the project directory. That can also be automatically downloaded when initialized

5. **Prepare Polygon Data:**

    - Create a `Space_ROIs` pickle file with a list of polygons (list of lists of tuples) representing parking spaces.

## Usage

1. **Run the ROI Reference Image Script:**

    If you need to create or update your polygon ROIs, use the provided script to capture reference images from the video. This script helps in defining the parking spaces in the form of polygons.

    ```bash
    python ParkingSpaceSelection.py
    ```

    Follow the prompts to draw and save polygons on the reference image in Pickle file.

2. **Run the Parking Space Detection Script:**

    ```bash
    python main.py
    ```

3. **Input Video:**

    Define input video dir e.g. `input_video/parking_space.mp4` in the appropriate directory. Modify the `cv2.VideoCapture` line in the script to match your video source if different.

4. **Exit the Video Feed:**

    Press `q` while the video window is active to quit the application.

## Code Overview

1. **Loading YOLO Model:**

   The YOLO model (`yolov8n.pt`) is loaded and moved to GPU if CUDA is available.

2. **Loading Polygon Data:**

   The parking space polygon data is loaded from a pickle file.

3. **Video Capture:**

   Captures video frames from a file or camera.

4. **Detection and Drawing:**

   YOLO performs object detection. Detected objects are checked against the predefined polygons to determine if they occupy parking spaces. The frame is annotated with bounding boxes and status updates.

5. **Display:**

   Displays the video feed with detected objects and parking slot status.

**Note** : Define ROIS on image extract from same video you want to run Scripts
