import os
from datetime import datetime

directory = "7_FilesDataManipulation/files"

filenames = os.listdir(directory)

for filename in filenames:
    filepath = os.path.join(directory, filename)

    with open(filepath) as file:
        content = file.read()
        words_count = len(content.split())

    day = datetime.now().strftime("%A")
    date = datetime.today().date()

    new_filename1 = f"{filename[:-4]}-{day}.txt"
    new_filename2 = f"{filename[:-4]}-{date}.txt"

    new_filepath1 = os.path.join(directory, new_filename1)
    new_filepath2 = os.path.join(directory, new_filename2)

    os.replace(filepath, new_filepath1)
    os.replace(filepath, new_filepath2)

    print(f"Renamed {filename} to {new_filename1}")
