import cv2
import numpy as np
from skimage import filters


# 处理NumPy数组图像
def edge_detection(image):
    # 确保图像是灰度格式
    if len(image.shape) == 3 and image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 使用 Sobel 方法进行边缘检测
    edges = filters.sobel(image)
    return edges
