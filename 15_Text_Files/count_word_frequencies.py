import glob

filepaths = sorted(glob.glob("15_Text_Files/*.txt"))

word_frequency = {}
for filepath in filepaths:
    with open(filepath) as file:
        content = file.read()
        words = content.split()

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1


with open("word_frequencies.txt", 'w') as file:
    for word, frequency in word_frequency.items():
        file.write(f"{word}: {frequency} \n")
