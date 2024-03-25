from ultralytics import YOLO
# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

source = 'C:/Users/limjiaquan/YOLOv8_data/cus_data/001.mp4'
model.predict( source, 
               save=True, 
               imgsz=640, 
               conf=0.5,
               classes = 0,
               save_txt=True,   # 设置 save_txt 为 True，以便生成 YOLO 的 txt 文件
               save_frames=False,# 設置 save_frames 為 True，是要創建datasets的意思，會保留檢測到的原始圖片
               )  
