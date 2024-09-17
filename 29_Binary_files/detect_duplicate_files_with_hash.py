import hashlib
import os


def get_content(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
        hash_value = hashlib.sha256(content).hexdigest()
    return hash_value


file_dir = os.walk('files')

file_content = {}
for root, dir, files in file_dir:
    for file in files:
        file_path = os.path.join(root, file)
        # print(file_path)
        file_hash_value = get_content(file_path)

        if file_hash_value in file_content:
            print("Duplicate file found", file_path)
            print("Original file found", file_content[file_hash_value])
            os.remove(file_path)
        else:
            file_content[file_hash_value] = file_path
