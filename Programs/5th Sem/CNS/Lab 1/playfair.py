#For the plaint given in question 1, apply Play Fair cipher encryption with key “WORK”.


def generate_pm(keyword):
    keyword = keyword.replace("J", "I").upper().replace(" ", "")
    keyword = "".join(filter(str.isalpha, keyword))
    matrix = []
    for char in keyword + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in matrix:
            matrix.append(char)
    pm = [matrix[i:i+5] for i in range(0, 25, 5)]
    return pm

def find_char_position(matrix, char):
    for row, row_chars in enumerate(matrix):
        if char in row_chars:
            return row, row_chars.index(char)

def playfair_process(t, keyword, dir):
    matrix = generate_pm(keyword)
    proc_t = ""
    i = 0
    while i < len(t):
        if i == len(t) - 1 or t[i] == t[i + 1]:
            t = t[:i + 1] + 'X' + t[i + 1:]
        i += 2

    if len(t) % 2 != 0: #append x if length is odd
        t += 'X'

    i = 0
    while i < len(t):
        char1, char2 = t[i], t[i + 1]
        row1, col1 = find_char_position(matrix, char1)
        row2, col2 = find_char_position(matrix, char2)
        if row1 == row2:
            proc_t += matrix[row1][(col1 + dir) % 5] + matrix[row2][(col2 + dir) % 5]
        elif col1 == col2:
            proc_t += matrix[(row1 + dir) % 5][col1] + matrix[(row2 + dir) % 5][col2]
        else:
            proc_t += matrix[row1][col2] + matrix[row2][col1]
        i += 2

    return proc_t

def playfair_encrypt(t, keyword):
    return playfair_process(t, keyword, 1)

def playfair_decrypt(t, keyword):
    return playfair_process(t, keyword, -1)


user_input = input("Enter the string you want to encrypt: ").upper()
key = input("Enter the key (a keyword without spaces): ")

encrypted_result = playfair_encrypt(user_input, key)

print("Encrypted text:", encrypted_result)
print("Decrypted text:", playfair_decrypt(encrypted_result, key))