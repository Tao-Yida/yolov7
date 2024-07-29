import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
image_path = "../Massachusetts-Buildings-Dataset/tiff/images/train/22678915_15_1_2.tiff"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

# Read YOLO format label
label_path = "../Massachusetts-Buildings-Dataset/tiff/labels/train/22678915_15_1_2.txt"
with open(label_path, "r") as file:
    lines = file.readlines()

# Draw bounding boxes on the image
for line in lines:
    line = line.strip().split()
    class_id = int(line[0])
    x, y, w, h = map(float, line[1:])
    x1 = int((x - w / 2) * image.shape[1])
    y1 = int((y - h / 2) * image.shape[0])
    x2 = int((x + w / 2) * image.shape[1])
    y2 = int((y + h / 2) * image.shape[0])
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Display the image
plt.imshow(image)
plt.show()