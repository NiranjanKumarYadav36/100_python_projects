import glob

filepaths = sorted(glob.glob("*.txt"))

content_list = []
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
        content_list.append(content)


with open("merged_file.txt", 'w') as file:
    for content in content_list:
        file.write(content + '\n')
