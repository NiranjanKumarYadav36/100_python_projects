class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            text = file.read()

        return text

    def write_file(self, content):
        with open(f"capitalize_{self.file_path}", 'w') as file:
            file.write(content)


class Text:
    def __init__(self, input_text):
        self.input_text = input_text

    def capitalize_letter(self):
        sentences = self.input_text.split('.')
        capitalize_sentence = []
        for sentence in sentences:
            sentence = sentence.strip().capitalize()
            capitalize_sentence.append(sentence)

        capitalize_sentence = ". ".join(capitalize_sentence)

        return capitalize_sentence


file = File('snowwhite.txt')
content = file.read_file()

text = Text(content)
capitalized_text = text.capitalize_letter()

file.write_file(capitalized_text)
