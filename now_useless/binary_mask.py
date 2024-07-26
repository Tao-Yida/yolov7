import cv2
import numpy as np
import os
import csv


def extract_borders_from_image(image_path):
    # 读取图片
    image = cv2.imread(image_path, 0)

    # 将图片二值化
    _, binary_mask = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

    # 查找二值化图片中的轮廓
    contours, _ = cv2.findContours(
        binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    # 初始化一个列表来存储建筑边框的坐标
    building_borders = []

    # 遍历每一个找到的轮廓并提取其坐标
    for contour in contours:
        # 为每个轮廓创建一个边界矩形
        x, y, w, h = cv2.boundingRect(contour)

        # 存储每个边界框的坐标（表示建筑边框）
        building_borders.append((x, y, x + w, y + h))

    return building_borders


def process_images_in_folder(folder_path, output_csv):
    # 获取文件夹中的所有PNG文件
    image_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]

    # 打开CSV文件准备写入
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        # 写入CSV文件的表头
        writer.writerow(["image_name", "x1", "y1", "x2", "y2"])

        # 处理每一张图片
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            borders = extract_borders_from_image(image_path)

            # 写入每个边框的数据到CSV文件
            for border in borders:
                writer.writerow([image_file, *border])


# 设置标签图片文件夹路径和输出CSV文件路径
label_folder = "../Massachusetts Buildings Dataset/png/train_labels"
output_csv = "../Massachusetts Buildings Dataset/train_labels.csv"

# 处理文件夹中的所有图片并将边框数据存入CSV文件
if __name__ == "__main__":
    process_images_in_folder(label_folder, output_csv)
