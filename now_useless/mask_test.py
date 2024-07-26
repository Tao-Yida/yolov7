import cv2
import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
csv_file = '../Massachusetts Buildings Dataset/train_labels.csv'
data = pd.read_csv(csv_file)

# 筛选出所有 image_name 为 23579065_15.png 的行
filtered_data = data[data['image_name'] == '23579065_15.png']

# 读取原始图片
image_path = '../Massachusetts Buildings Dataset/png/train/23579065_15.png'
image = cv2.imread(image_path)

# 遍历每一行数据并绘制矩形
for index, row in filtered_data.iterrows():
    x1, y1, x2, y2 = row['x1'], row['y1'], row['x2'], row['y2']
    # 绘制矩形
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

# 显示图片
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
