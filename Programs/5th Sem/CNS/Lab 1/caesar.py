# For the given input, perform Caesar cipher encryption and decryption.
# Plain text: “CRYPTOGRAPHY”
# Key: 10

def caesar_encrypt(pt):
    et = list(pt)
    for i in range(0,len(et)):
        char = et[i]
        if char.isalpha():
            if char.islower():
                et[i] = chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
            else:
                et[i] = chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
        else:
            continue
    return ("".join(et))

def caesar_decrypt(et):
    dt = list(et)
    for i in range(0,len(dt)):
        char = dt[i]
        if char.isalpha():
            if char.islower():
                dt[i] = chr((ord(char) - ord('a' ) - shift) % 26 + ord('a'))
            else:
                dt[i] = chr((ord(char) - ord('A' ) - shift) % 26 + ord('A'))
        else:
            continue
    return ("".join(dt))

user_input = input("Enter the string to be encrypted: ")
key = int(input("Enter the key (integer shift value): "))
shift = key % 26

er = caesar_encrypt(user_input)
dr = caesar_decrypt(er)

print("Encrypted Text:", er)
print("Decrypted Text:", dr)
