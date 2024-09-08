# List of most frequent letters in the English language, in order of frequency
frequency_list = ['e', 't', 'a', 'u', 'l', 'm', 'f', 'y', 'w', 'i', 'g', 'p', 'b', 'v', 'k', 'x', 'q', 'j', 'z']


# Function to find the most frequent character in the cipher text
def most_freqeuent_number(lst):
    freq_dic = {}

    # Count the occurrences of each character in the list
    for num in lst:
        if num not in freq_dic:
            freq_dic[num] = 1
        else:
            freq_dic[num] += 1

    # Return the character with the maximum frequency
    most_frequent = max(freq_dic, key=freq_dic.get)
    return most_frequent


# Cipher text to be decrypted
cipher_text = (input(f"Enter the cipher text: ").lower().replace(" ", "")
               .strip())  # Remove spaces, convert to lowercase, and strip leading/trailing whitespace
# print(cipher_text)

# Split cipher text into a list of characters
cipher_text = list(cipher_text)
# print(cipher_text)

# Convert each character in the cipher text to its ASCII value
cipher_text_ascii = [ord(c) for c in cipher_text]
# print(cipher_text_ascii)

# Find the most frequent character in the cipher text (in ASCII form)
most_common_character = most_freqeuent_number(cipher_text_ascii)
# print("Most common character (ASCII):", most_common_character)

# Try to decrypt the cipher text assuming the most frequent letter in the cipher corresponds to each letter in 'frequency_list'
for i in frequency_list:
    decrypted_list = []

    # Calculate the shift (difference) between the most common character in the cipher and the current letter in 'frequency_list'
    diff = most_common_character - ord(i)

    # Decrypt each character in the cipher text by applying the calculated shift
    for j in range(len(cipher_text_ascii)):
        decrypt_character = chr(
            ((cipher_text_ascii[j] - diff - 97) % 26) + 97)  # Adjust shift and wrap-around using modulo
        decrypted_list.append(decrypt_character)

    # Join the list of decrypted characters into a string
    decrypt_text = "".join(decrypted_list)

    # Display the attempted decryption
    print("Attempted Decryption:", decrypt_text)

    # Ask the user if the current decryption attempt is correct
    answer_check = input("Is this correct? (Y/N): ").lower()
    if answer_check == "y":
        break  # Exit the loop if the decryption is confirmed correct
