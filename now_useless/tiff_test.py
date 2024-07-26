import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取CSV文件
file_path = 'raster_data_label.csv'
raster_data = pd.read_csv(file_path)

# 提取经纬度和栅格值
longitudes = raster_data['Longitude']
latitudes = raster_data['Latitude']
values = raster_data['Value']

# 绘制栅格图
plt.figure(figsize=(10, 8))
sc = plt.scatter(longitudes, latitudes, c=values, cmap='viridis', s=1)
plt.colorbar(sc, label='Value')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Raster Data Visualization')
plt.show()