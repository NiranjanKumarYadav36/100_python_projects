import os
import shutil

dir_path = 'Downloads'

for root, dir, files in os.walk(dir_path):
    # print("root", root)
    # print("dir", dir)
    # print("files", files)

    for file in files:
        file_path = os.path.join(root, file)
        os.remove(file_path)
        # shutil.move(file_path, os.path.join('backup', file))

    for d in dir:
        file_path = os.path.join(root, d)
        shutil.rmtree(file_path)
