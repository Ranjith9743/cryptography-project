import numpy as np

def text_to_numbers(text):
    """Convert A=0, B=1, ... Z=25"""
    return [ord(c) - ord('A') for c in text.upper() if c.isalpha()]

def numbers_to_text(nums):
    """Convert numbers back to letters"""
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

def create_key_matrix(key):
    """Create a 2x2 matrix from a 4-letter key"""
    key = key.upper()
    nums = text_to_numbers(key)
    if len(nums) < 4:
        raise ValueError("Key must be at least 4 letters for 2x2 Hill cipher")
    return np.array(nums[:4]).reshape(2, 2)

def check_invertible_mod26(matrix):
    """Check if matrix is invertible mod 26"""
    det = int(round(np.linalg.det(matrix))) % 26
    try:
        det_inv = pow(det, -1, 26)  # modular inverse
    except ValueError:
        return None  # not invertible
    return det_inv

def encrypt(message, key):
    key_matrix = create_key_matrix(key)
    msg_nums = text_to_numbers(message)

    # pad message if odd length
    if len(msg_nums) % 2 != 0:
        msg_nums.append(ord('X') - ord('A'))

    result = []
    for i in range(0, len(msg_nums), 2):
        pair = np.array(msg_nums[i:i+2])
        enc = np.dot(key_matrix, pair) % 26
        result.extend(enc)
    return numbers_to_text(result)

def decrypt(cipher, key):
    key_matrix = create_key_matrix(key)

    # Check invertibility
    det_inv = check_invertible_mod26(key_matrix)
    if det_inv is None:
        raise ValueError("Invalid key: matrix is not invertible modulo 26")

    # Compute inverse matrix mod 26
    det = int(round(np.linalg.det(key_matrix))) % 26
    adj = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    inv_matrix = (det_inv * adj) % 26

    cipher_nums = text_to_numbers(cipher)
    result = []
    for i in range(0, len(cipher_nums), 2):
        pair = np.array(cipher_nums[i:i+2])
        dec = np.dot(inv_matrix, pair) % 26
        result.extend(dec)
    return numbers_to_text(result)
