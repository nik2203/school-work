import numpy as np

# Helper function to convert plaintext to numerical form
def text_to_num(plaintext, size):
    # Convert plaintext to uppercase
    plaintext = plaintext.upper()
    # Remove all non-alphabetic characters
    plaintext = ''.join(filter(str.isalpha, plaintext))
    # Pad plaintext with X if necessary
    if len(plaintext) % size != 0:
        plaintext += 'X' * (size - len(plaintext) % size)
    # Convert plaintext to numerical form
    numtext = []
    for i in range(0, len(plaintext), size):
        block = plaintext[i:i+size]
        blocknum = []
        for c in block:
            blocknum.append(ord(c) - ord('A'))
        numtext.append(blocknum)
    return np.array(numtext, dtype=np.float64)

# Helper function to convert numerical form to plaintext
def num_to_text(numtext):
    # Convert numerical form to plaintext
    plaintext = ""
    for blocknum in numtext:
        block = ""
        for num in blocknum:
            block += chr(int(num) + ord('A'))
        plaintext += block
    return plaintext

# Hill cipher encryption function
def hill_encrypt(plaintext, key):
    size = key.shape[0]
    numtext = text_to_num(plaintext, size)
    ciphertext = []
    for blocknum in numtext:
        blocknum = np.array(blocknum).reshape((size, 1))
        blocknum_encrypted = key.dot(blocknum).astype(np.int64) % 26
        ciphertext.append(blocknum_encrypted.flatten().tolist())
    return num_to_text(np.array(ciphertext))

# Hill cipher decryption function
def hill_decrypt(ciphertext, key):
    size = key.shape[0]
    numtext = text_to_num(ciphertext, size)
    plaintext = ciphertext
    p1aintext = []
    key_inv = np.linalg.inv(key)
    for blocknum in numtext:
        blocknum = np.array(blocknum).reshape((size, 1))
        blocknum_decrypted = key_inv.dot(blocknum).astype(np.int64) % 26
        p1aintext.append(blocknum_decrypted.flatten().tolist())
        plaintext = ciphertext.upper()
    return plaintext

# Example usage
key = np.array([[3, 10], [20, 9]])
plaintext = input("Enter plaintext: ")
ciphertext = hill_encrypt(plaintext, key)
print("\nPlaintext: ", plaintext)
print("Ciphertext:", ciphertext)
decrypted_text = hill_decrypt(plaintext, key)
print("Decrypted text: ", decrypted_text)
