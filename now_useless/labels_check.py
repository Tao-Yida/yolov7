import os

image_folder = '../Massachusetts-Buildings-Dataset/png/train'
label_folder = '../Massachusetts-Buildings-Dataset/png/train_labels_yolo'

images = set(os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.endswith('.png'))
labels = set(os.path.splitext(f)[0] for f in os.listdir(label_folder) if f.endswith('.txt'))

missing_labels = images - labels
missing_images = labels - images

if missing_labels:
    print(f"Missing labels for images: {missing_labels}")
if missing_images:
    print(f"Missing images for labels: {missing_images}")

assert not missing_labels and not missing_images, "Image-label pairs are mismatched."


for label_file in os.listdir(label_folder):
    if label_file.endswith('.txt'):
        with open(os.path.join(label_folder, label_file)) as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split()
                assert len(parts) == 5, f"Incorrect label format in {label_file}: {line}"
                assert parts[0] == '0', f"Incorrect class label in {label_file}: {line}"
                for value in parts[1:]:
                    assert 0 <= float(value) <= 1, f"Value out of range in {label_file}: {line}"

print("All labels are in correct format.")