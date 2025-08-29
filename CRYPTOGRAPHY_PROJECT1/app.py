from flask import Flask, render_template, request
from ciphers.vigenere import encrypt as vigenere_encrypt, decrypt as vigenere_decrypt
from ciphers.playfair import encrypt as playfair_encrypt, decrypt as playfair_decrypt
from ciphers.hill import encrypt as hill_encrypt, decrypt as hill_decrypt
from ciphers.blowfish import encrypt as blowfish_encrypt, decrypt as blowfish_decrypt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    message = ""
    key = ""
    selected_cipher = "vigenere"
    action = "encrypt"
    error = ""

    if request.method == 'POST':
        message = request.form.get('message', '')
        key = request.form.get('key', '')
        selected_cipher = request.form.get('cipher', 'vigenere')
        action = request.form.get('action', 'encrypt')

        try:
            if selected_cipher == "vigenere":
                result = vigenere_encrypt(message, key) if action == "encrypt" else vigenere_decrypt(message, key)

            elif selected_cipher == "playfair":
                result = playfair_encrypt(message, key) if action == "encrypt" else playfair_decrypt(message, key)

            elif selected_cipher == "hill":
                result = hill_encrypt(message, key) if action == "encrypt" else hill_decrypt(message, key)

            elif selected_cipher == "blowfish":
                result = blowfish_encrypt(message, key) if action == "encrypt" else blowfish_decrypt(message, key)

        except Exception as e:
            error = str(e)   # capture error message

    return render_template(
        'index.html',
        result=result,
        message=message,
        key=key,
        selected_cipher=selected_cipher,
        action=action,
        error=error
    )

if __name__ == '__main__':
    app.run(debug=True)

