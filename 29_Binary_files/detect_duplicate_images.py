import os
import imagehash
from PIL import Image


def get_content(path):
    with Image.open(path) as img:
        image_hash = str(imagehash.average_hash(img, hash_size=8))
    return image_hash


photos_dir = 'img_file'
filepath = os.walk(photos_dir)

hashes = {}
for root, dir, files in filepath:
    for file in files:
        file_path = os.path.join(root, file)

        img_hash = get_content(file_path)

        if img_hash in hashes:
            print("Duplicate Image found", file_path)
            print("Original Image", hashes[img_hash])
            os.remove(file_path)
        else:
            hashes[img_hash] = file_path
