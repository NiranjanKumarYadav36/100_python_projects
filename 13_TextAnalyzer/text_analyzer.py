def remove_punctuation(text):
    punctuations = "{,!#}@*&%."
    for char in punctuations:
        text = text.replace(char, "")
    return text


def characters_count(text):
    characters = len(text.strip())
    return characters


def words_count(text):
    words = text.split()
    return len(words)


def sentences_count(text):
    text = text.strip()
    sentence = text.count(".") + text.count("!") + text.count("?")
    return sentence


def most_frequent_word(text):
    new_text = remove_punctuation(text)
    new_text = new_text.lower().strip().split()
    frequency_of_words = {}
    for item in new_text:
        if item not in frequency_of_words:
            frequency_of_words[item] = 1
        else:
            frequency_of_words[item] += 1

    most_frequent = max(frequency_of_words, key=frequency_of_words.get)
    return most_frequent


def avg_word_length(text):
    text = text.strip().split()
    lengths = [len(word) for word in text if word]
    return sum(lengths) / len(lengths)


text = input("enter a block of text for analysis:\n")

print(f"Text Analysis result")
print("-" * 20)
print("Total Characters:", characters_count(text))
print("Total Words:", words_count(text))
print("Total Sentences:", sentences_count(text))
print(f"Most Frequent Word: {most_frequent_word(text)}")
print("Average Word length", avg_word_length(text))
# print("Average Sentence Length", )


"""
The Laysan honeycreeper (Himatione fraithii) is an extinct species of finch, first recorded in 1828, that was endemic to Laysan in the Northwestern Hawaiian Islands. Its length was 13–15 cm (5–6 in) with a 64–69 mm long (2.5–2.7 in) wing. It was bright scarlet vermilion with a faint tint of golden orange on the head, breast and upper abdomen; the rest of its upper parts were orange scarlet. The lower abdomen was dusky gray fading into brownish white. The wings, tail, bill, and legs were dark brown. The bill was slender and downturned. It was nectarivorous and insectivorous, gathering nectar and insects from flowers. The breeding season was probably between January and June, and the clutch size was four or five eggs. In 1903, domestic rabbits were introduced to the island and destroyed its vegetation. In April 1923, only three Laysan honeycreepers were found, one of which was filmed. On April 23, a sandstorm hit the island, and the last birds perished due to lack of cover. 
"""