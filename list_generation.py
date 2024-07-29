import os

# Usage example
folder_path = "../FaceMask_Dataset/images/test"
output_file = "../FaceMask_Dataset/test.txt"

def save_file_paths(folder_path, output_file):
    with open(output_file, "w") as file:
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                # Check if the file is an image
                if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    file_path = os.path.join(root, file_name)
                    relative_path = os.path.relpath(file_path, folder_path)
                    file.write(os.path.join(folder_path, relative_path) + "\n")

save_file_paths(folder_path, output_file)