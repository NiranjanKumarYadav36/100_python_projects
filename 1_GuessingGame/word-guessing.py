import random

# List of words to guess from
words = ["python", "java", "swift", "javascript", "ruby"]

# Randomly selecting the position of the word
# random_word = random.choice(words)
random_word_position = random.randint(0, len(words) - 1)

# Decreasing the word position by 1 (this may cause an issue if random_word_position is 0)
random_word_position -= 1

max_attempt = 6
attempt_count = 0

# Welcome message and instructions for the game
print(f"Welcome to the Word Guessing Game!")
print(f"I have selected a word from a list of programming languages.")
print(f"You have {max_attempt} attempts to guess the correct word")

# Main game loop, which runs for 'max_attempt' attempts
for i in range(max_attempt):
    guess_word = input(f"Enter your word: ").lower()  # Converting guess to lowercase

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
    print(f"You have used all your attempts. The correct word is '{words[random_word_position]}'")
