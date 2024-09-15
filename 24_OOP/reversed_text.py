class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as file:
            text = file.read()
        return text

    def write_file(self, content):
        with open(f"reversed{self.file_path}", 'w') as file:
            file.write(content)


class Text:
    def __init__(self, input_text):
        self.input_text = input_text

    def reversed_words(self):
        text = self.input_text
        words = text.split()

        reversed_word = []

        for t in words:
            reversed_word.append(t[::-1])

        reversed_word = "".join(reversed_word)

        return reversed_word


file = File('example.txt')
content = file.read_file()

text = Text(content)
reversed_text = text.reversed_words()

file.write_file(reversed_text)
