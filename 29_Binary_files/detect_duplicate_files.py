import os

fie_path = os.walk('files')


def get_content(filepath):
    with open(filepath, 'rb') as file:
        content = file.read()
    return content


file_contents = {}


for root, dir, files in fie_path:
    print(root, dir, files)
    for file in files:
        # print(file)
        filepath = os.path.join(root, file)
        # print(filepath)
        content = get_content(filepath)
        # print(content)
        if content in file_contents:
            print("Duplicate found", filepath)
            print("Original file", file_contents[content])
            os.remove(filepath)
        else:
            file_contents[content] = filepath

# print(file_contents)
