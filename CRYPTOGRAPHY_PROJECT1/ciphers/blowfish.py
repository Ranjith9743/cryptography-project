from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(message, key):
    key = key.encode("utf-8")
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_text = pad(message.encode("utf-8"), Blowfish.block_size)
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted).decode("utf-8")

def decrypt(ciphertext, key):
    key = key.encode("utf-8")
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decoded = base64.b64decode(ciphertext)
    decrypted = unpad(cipher.decrypt(decoded), Blowfish.block_size)
    return decrypted.decode("utf-8")
