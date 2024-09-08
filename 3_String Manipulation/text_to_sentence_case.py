# Read the text from the file
with open("snowwhite.txt", 'r') as file1:
    text = file1.read()

# Split the text into sentences
sentences = text.split('.')
print(sentences)


capitalize_sentences = [sentence.strip().capitalize() for sentence in sentences if sentence]
print(capitalize_sentences)

new_text = '. '.join(capitalize_sentences)
print(new_text)

with open("corrected_snowwhite.txt", 'w') as file2:
    file2.write(new_text)





















