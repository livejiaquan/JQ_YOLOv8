import argparse
from ultralytics import YOLO

def main(source):
    # Load a pretrained YOLOv8n model
    model = YOLO(R'\Users\limjiaquan\anaconda\envs\YOLOv8env\Lib\site-packages\ultralytics\yolov8s-world.pt')

    model.predict(source, 
                   save=True, 
                   imgsz=640, 
                   conf=0.6,
                   classes=0,
                   save_txt=True,   # Set save_txt to True to generate YOLO txt files
                   save_frames=True # Set save_frames to True to create datasets, it will keep detected original images
                   )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YOLOv8n object detection')
    parser.add_argument('--source', type=str, required=True, help='Source for object detection (e.g., RTSP URL, file path)')
    
    args = parser.parse_args()
    main(args.source)
