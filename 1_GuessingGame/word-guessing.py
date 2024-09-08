import random

words = ["python", "java", "swift", "javascript", "ruby"]

# random_word = random.choice(words)

random_word_position = random.randint(0, len(words)-1)
random_word_position -= 1
# print(random_word_position)
max_attempt = 6
attempt_count = 0

print(f"Welcome to the Word Guessing Game!")
print(f"I have selected a word from a list of programming languages.")
print(f"You have {max_attempt} attempts to guess the correct word")


for i in range(max_attempt):
    guess_word = input(f"Enter your word: ")
    guess_word = guess_word.lower()
    attempt_count += 1
    if len(guess_word) < len(words[random_word_position]):
        print(f"Your guess is shorter than the correct word. Try again.")
    elif len(guess_word) > len(words[random_word_position]):
        print(f"Your guess is longer than the correct word. Try again.")
    else:
        print(f"Congratulations! You have guessed the correct word '{words[random_word_position]}' "
              f"in {attempt_count} attempts")
        break;

else:
    print(f"You have used your all attempts. The correct word is '{words[random_word_position]}'")
