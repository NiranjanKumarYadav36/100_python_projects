
def remove_duplicates(keyword):
    result = []
    for char in keyword:
        if char not in result:
            result.append(char)

    # print(result)
    # print(''.join(result))
    return ''.join(result)


def generate_matrix(keyword, alphabet):
    new_keyword = remove_duplicates(keyword)

    key_alphabet = [char for char in alphabet if char not in new_keyword]
    key_alphabet = ''.join(key_alphabet)

    combined_key = new_keyword + key_alphabet

    # Create 5x5 matrix
    matrix = [list(combined_key[i:i + 5]) for i in range(0, 25, 5)]
    char_positions = {}
    for row in range(5):
        for col in range(5):
            char_positions[matrix[row][col]] = (row, col)
    # print(char_positions)

    return matrix, char_positions


def make_pairs(message):
    message = list(message)
    i = 0
    # print(len(message))

    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message.insert(i + 1, 'x')
            i += 1
        i += 1

    if len(message) % 2 != 0:
        message.append('x')

    # print(message)
    return message


def process_pairs(pairs, matrix, character_positions):
    encrypted_text = []
    for i in range(0, len(pairs) - 1, 2):
        # print(i)
        pair = (pairs[i], pairs[i + 1])
        # print(pair)

        encrypted_pair = encryption(pair, matrix, character_positions)

        # print(encrypted_pair)
        encrypted_text.append(encrypted_pair)

    encrypted_text = "".join(encrypted_text)
    print(f"Cipher Text: {encrypted_text}")


def encryption(pair, matrix, character_positions):
    pos1 = character_positions.get(pair[0])
    pos2 = character_positions.get(pair[1])
    # print(pos1, pos2)

    if pos1[0] == pos2[0]:
        # print("same row")
        pos1_new_pos = (pos1[0], pos1[0 + 1])
        pos2_new_pos = (pos2[0], pos2[0 + 1])

    elif pos1[1] == pos2[1]:
        # print("same cloumn")
        pos1_new_pos = ((pos1[0] + 1), pos1[1])
        pos2_new_pos = ((pos2[0] + 1), pos2[1])

    else:
        # print("Rectangle")
        pos1_new_pos = (pos1[0], pos2[1])
        pos2_new_pos = (pos2[0], pos1[1])
        # print(pos1_new_pos, pos2_new_pos)

    encrypted_pair = matrix[pos1_new_pos[0]][pos1_new_pos[1]] + matrix[pos2_new_pos[0]][pos2_new_pos[1]]
    # print(encrypted_pair)

    return encrypted_pair


alphabet = 'abcdeifghiklmnopqrstuvwxyz'
message = input("Enter message: ").lower().strip()
message = message.split()
for i in message:
    if i == 'j':
        index = message.index(i)
        message[index] = 'i'
print(message)
keyword = input("Enter Keyword: ").lower().strip()
keyword = keyword.split()
for char in keyword:
    if char == 'j':
        index = keyword.index(char)
        char = 'i'
print(keyword)
# generate matrix
matrix, character_positions = generate_matrix(keyword, alphabet)
# print(matrix)
# print(character_positions)
pairs = make_pairs(message)
# print(pairs)

process_pairs(pairs, matrix, character_positions)

