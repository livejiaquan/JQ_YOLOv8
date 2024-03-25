from ultralytics import YOLO
from pathlib import Path
import cv2

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

source = '/Users/limjiaquan/YOLOv8_data/cus_data/001.mp4'

# Run inference
results = model(source, 
                save=True, 
                imgsz=320, 
                conf=0.5,
                classes=0,
                save_txt=True,   # Save YOLO txt files
                save_crop=False)  # Do not save cropped images

# Get the path to the predict directory
predict_dir = results.results_dir.parent

# Define the path to save the images
save_dir = predict_dir / "images"

# Function to save detected objects' images
def save_detected_objects_images(save_dir, frame_number, results):
    for result in results.xyxy:
        img = cv2.cvtColor(result["image"], cv2.COLOR_RGB2BGR)
        file_name = save_dir / f"frame_{frame_number}_obj_{result['class']}.jpg"
        cv2.imwrite(str(file_name), img)

# Create the directory to save images
save_dir.mkdir(parents=True, exist_ok=True)

# Open video source
cap = cv2.VideoCapture(source)

# Read and process each frame
frame_number = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Save detected objects' images
    save_detected_objects_images(save_dir, frame_number, results[frame_number])
    
    frame_number += 1

cap.release()
cv2.destroyAllWindows()
