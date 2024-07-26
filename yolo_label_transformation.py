import os
import cv2
import rasterio


def create_yolo_labels(tiff_path, yolo_label_path):
    with rasterio.open(tiff_path) as src:
        img = src.read(1)  # 读取第一个波段
        h, w = img.shape

        # 寻找轮廓
        contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        with open(yolo_label_path, "w") as f:
            for contour in contours:
                # 获取轮廓的边界框
                x, y, w_box, h_box = cv2.boundingRect(contour)
                x_center = (x + w_box / 2) / w
                y_center = (y + h_box / 2) / h
                width = w_box / w
                height = h_box / h
                f.write(f"0 {x_center} {y_center} {width} {height}\n")


label_folder = "../Massachusetts-Buildings-Dataset/tiff/test_labels_split"
yolo_label_folder = "../Massachusetts-Buildings-Dataset/tiff/test_labels_split_yolo"

if not os.path.exists(yolo_label_folder):
    os.makedirs(yolo_label_folder)

for label_file in os.listdir(label_folder):
    if label_file.endswith(".tif") or label_file.endswith(".tiff"):
        tiff_path = os.path.join(label_folder, label_file)
        yolo_label_path = os.path.join(
            yolo_label_folder, os.path.splitext(label_file)[0] + ".txt"
        )
        create_yolo_labels(tiff_path, yolo_label_path)
