from ultralytics import YOLO
# Load a pretrained YOLOv8n model
model = YOLO('yolov8m.pt')

source = '/Users/limjiaquan/YOLOv8_data/cus_data/001.mp4'
model.predict( source, 
               save=True, 
               imgsz=320, 
               conf=0.5,
               classes = 0,
               save_txt=True,   # 设置 save_txt 为 True，以便生成 YOLO 的 txt 文件
               save_crop=True,
               save_img=False
               )  
