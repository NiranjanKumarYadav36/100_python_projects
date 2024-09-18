import os
import re

directory = 'text'
filenames = os.listdir(directory)

first_sentences = []
for filename in filenames:
    filepath = os.path.join(directory, filename)

    with open(filepath, 'r') as file:
        content = file.read()
        pattern = r'[a-zA-Z0-9,;"\'\s\-()_]+[.!?]'
        sentences = re.findall(pattern, content)
        first_sentences.append(sentences[0])


# Print all first sentences one in each line
for sentence in first_sentences:
    print(sentence)