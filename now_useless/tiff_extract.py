import os
import torch
from osgeo import gdal

def extract_raster_data_from_folder(folder_path):
    # 初始化一个列表来存储所有文件的栅格数据
    all_raster_data = []

    # 遍历文件夹中的所有TIFF文件
    for filename in os.listdir(folder_path):
        if filename.endswith(".tif") or filename.endswith(".tiff"):
            tiff_file = os.path.join(folder_path, filename)
            print(f"Processing file: {tiff_file}")
            
            # 打开TIFF文件
            dataset = gdal.Open(tiff_file)
            
            # 获取地理信息
            geo_transform = dataset.GetGeoTransform()
            x_origin = geo_transform[0]
            y_origin = geo_transform[3]
            pixel_width = geo_transform[1]
            pixel_height = geo_transform[5]
            
            # 获取栅格数据
            band = dataset.GetRasterBand(1)
            data = band.ReadAsArray()
            
            rows, cols = data.shape
            
            # 初始化一个张量来存储当前TIFF文件的栅格和坐标信息
            raster_data = torch.zeros((rows, cols, 3))
            
            for row in range(rows):
                for col in range(cols):
                    x = x_origin + col * pixel_width
                    y = y_origin + row * pixel_height
                    value = data[row, col]
                    raster_data[row, col] = torch.tensor([x, y, value])
            
            # 将当前TIFF文件的数据存储到总列表中
            all_raster_data.append(raster_data)
            print(f"Complete file: {tiff_file}")
    
    return all_raster_data