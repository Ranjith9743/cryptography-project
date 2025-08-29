def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    result = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    result = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            result += char
    return result
