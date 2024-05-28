from ultralytics import YOLO
# Load a pretrained YOLOv8n model
model = YOLO(r'C:\Users\limjiaquan\YOLOv8_data\cus_data\01_Project\yolov8-streamlit-detection-tracking\weights\pre_helmet.pt')
# source = 'rtsp://admin:tkec1234@10.47.170.119:554/cam/realmonitor?channel=1&subtype=0'
# source = 'rtsp://admin:tkec1234@10.47.170.116:554/cam/realmonitor?channel=1&subtype=0'
# source = r'\Users\limjiaquan\YOLOv8_data\cus_data\01_Project\00\runs\detect\predict18\rgbcam_frames'
source = r'C:\Users\limjiaquan\YOLOv8_data\0513\person\images'
model.predict( source, 
               save=True, 
               imgsz=640, 
               conf=0.5,
            #    classes = 1,
               save_txt=True,   # 设置 save_txt 为 True，以便生成 YOLO 的 txt 文件
               save_frames=False# 設置 save_frames 為 True，是要創建datasets的意思，會保留檢測到的原始圖片
               )  
