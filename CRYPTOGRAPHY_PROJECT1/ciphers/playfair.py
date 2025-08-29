import string

def generate_key_square(key):
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))
    alphabet = "".join(ch for ch in string.ascii_uppercase if ch != "J")
    key_square = key + "".join(ch for ch in alphabet if ch not in key)
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def format_message(message):
    message = message.upper().replace("J", "I").replace(" ", "")
    formatted = ""
    i = 0
    while i < len(message):
        a = message[i]
        b = message[i+1] if i+1 < len(message) else "X"
        if a == b:
            formatted += a + "X"
            i += 1
        else:
            formatted += a + b
            i += 2
    if len(formatted) % 2 != 0:
        formatted += "X"
    return formatted

def find_position(square, char):
    for row in range(5):
        for col in range(5):
            if square[row][col] == char:
                return row, col
    return None

def encrypt(message, key):
    square = generate_key_square(key)
    message = format_message(message)
    result = ""
    for i in range(0, len(message), 2):
        a, b = message[i], message[i+1]
        row1, col1 = find_position(square, a)
        row2, col2 = find_position(square, b)
        if row1 == row2:
            result += square[row1][(col1+1)%5] + square[row2][(col2+1)%5]
        elif col1 == col2:
            result += square[(row1+1)%5][col1] + square[(row2+1)%5][col2]
        else:
            result += square[row1][col2] + square[row2][col1]
    return result

def decrypt(message, key):
    square = generate_key_square(key)
    result = ""
    for i in range(0, len(message), 2):
        a, b = message[i], message[i+1]
        row1, col1 = find_position(square, a)
        row2, col2 = find_position(square, b)
        if row1 == row2:
            result += square[row1][(col1-1)%5] + square[row2][(col2-1)%5]
        elif col1 == col2:
            result += square[(row1-1)%5][col1] + square[(row2-1)%5][col2]
        else:
            result += square[row1][col2] + square[row2][col1]
    return result
