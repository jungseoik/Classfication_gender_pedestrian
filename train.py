from ultralytics import YOLO

model = YOLO("yolov8m-cls.pt")  
model.train(cfg="gender_cls.yaml")