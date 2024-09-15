import matplotlib.pyplot as plt

filepath = "data.txt"

with open(filepath, 'r') as file:
    data = file.readlines()  # give the data in list

data = [float(item.strip()) for item in data if item]

plt.figure(figsize=(10, 6))

plt.plot(data, marker='o', linestyle='dotted', color='b')
plt.title('Data from text file')
plt.xlabel('Index')
plt.ylabel('Value')
plt.grid(True)
plt.tight_layout()
plt.show()
