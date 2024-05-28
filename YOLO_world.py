from ultralytics import YOLO

# Initialize a YOLO-World model
model = YOLO("yolov8s-world.pt")  # or choose yolov8m/l-world.pt

# Define custom classes
model.set_classes(["blue-helmet"])

# Execute prediction for specified categories on an image
results = model.predict(r"C:\Users\limjiaquan\YOLOv8_data\test_ppe\cam17_20240429_1004\images\54.jpg")

# Show results
results[0].show()