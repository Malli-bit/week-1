import os
import zipfile
from PIL import Image


zip_path = "resize images/archive.zip"
extract_dir = "resize_images/extracted"
resize_dir = "resize_images/resized"
resize_size = (224, 224)


os.makedirs(extract_dir, exist_ok=True)
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)
print(f" Unzipped to: {extract_dir}")


os.makedirs(resize_dir, exist_ok=True)


for root, dirs, files in os.walk(extract_dir):
    for file in files:
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            try:
                src_path = os.path.join(root, file)

               
                relative_path = os.path.relpath(root, extract_dir)
                target_dir = os.path.join(resize_dir, relative_path)
                os.makedirs(target_dir, exist_ok=True)

               
                img = Image.open(src_path).convert("RGB")
                img = img.resize(resize_size)

               
                save_path = os.path.join(target_dir, file)
                img.save(save_path)
            except Exception as e:
                print(f" Error with file {file}: {e}")

print(f" All images resized and saved in: {resize_dir}")
