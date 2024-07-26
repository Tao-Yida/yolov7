from PIL import Image
import os

def split_image(image_path, output_folder, rows, cols):
    img = Image.open(image_path)
    img_width, img_height = img.size
    tile_width = img_width // cols
    tile_height = img_height // rows
    base_name = os.path.splitext(os.path.basename(image_path))[0]

    for row in range(rows):
        for col in range(cols):
            left = col * tile_width
            upper = row * tile_height
            right = (col + 1) * tile_width
            lower = (row + 1) * tile_height
            tile = img.crop((left, upper, right, lower))
            tile_name = f"{base_name}_{row+1}_{col+1}.tiff"
            tile.save(os.path.join(output_folder, tile_name))

def process_folder(folder_path, output_folder, rows, cols):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(folder_path):
        if filename.endswith(".tiff") or filename.endswith(".tif"):
            split_image(os.path.join(folder_path, filename), output_folder, rows, cols)

# 使用示例
input_folder = "../Massachusetts-Buildings-Dataset/tiff/val"
output_folder = "../Massachusetts-Buildings-Dataset/tiff/val_split/"
rows, cols = 5, 5
process_folder(input_folder, output_folder, rows, cols)
