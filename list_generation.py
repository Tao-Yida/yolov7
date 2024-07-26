import os

# Usage example
folder_path = "../Massachusetts-Buildings-Dataset/tiff/images/val/"
output_file = "../Massachusetts-Buildings-Dataset/tiff/val_list.txt"


def save_file_paths(folder_path, output_file):
    with open(output_file, "w") as file:
        for root, dirs, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(file_path, folder_path)
                file.write(folder_path + relative_path + "\n")


save_file_paths(folder_path, output_file)
