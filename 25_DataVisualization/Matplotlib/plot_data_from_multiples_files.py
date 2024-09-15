import matplotlib.pyplot as plt
import glob

filepaths = glob.glob("Matplotlib/files/*.txt")

data_list = []
file_name = []
for filepath in filepaths:
    with open(filepath, 'r') as file:
        value = file.read()
        data_list.append(value)
    file_name.append(filepath[6:-4])

data_list = [float(item) for item in data_list if item]

plt.figure(figsize=(10, 5))

plt.plot(file_name, data_list, marker='o', linestyle='dotted', color='b')
plt.ylabel('Value')
plt.grid(True)
plt.tight_layout()
plt.xticks(rotation=45)

plt.show()
