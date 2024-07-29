import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图片
ori_image = cv2.imread('./inference/images/22828930_15.png', cv2.IMREAD_GRAYSCALE)
# 高斯模糊
gaussian_image = cv2.GaussianBlur(ori_image, (3, 3), 0)

# 高通滤波器
laplacian = cv2.Laplacian(gaussian_image, cv2.CV_64F)
highpass_image = cv2.convertScaleAbs(laplacian)

# 中值滤波器
median_image = cv2.medianBlur(highpass_image, 5)

# 对比度增强
clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(8,8))  # 减少对比度增强的强度
enhanced_image = clahe.apply(median_image)

# 显示原图和处理后的图像
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.imshow(ori_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Highpass Filter Image')
plt.imshow(highpass_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Median Filter Image')
plt.imshow(median_image, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Enhanced Image')
plt.imshow(enhanced_image, cmap='gray')
plt.axis('off')

plt.show()