def secret_cipher(text, shift=3):
    reversed_text = text[::-1]
    encrypted = ''.join(chr(ord(c) + shift) if c.isalpha() else c for c in reversed_text)
    return encrypted

def decrypt_cipher(text, shift=3):
    decrypted = ''.join(chr(ord(c) - shift) if c.isalpha() else c for c in text)
    return decrypted[::-1]

msg = "Привет, агент 007!"
enc = secret_cipher(msg)
dec = decrypt_cipher(enc)

print("Оригинал:", msg)
print("Шифр:", enc)
print("Расшифровка:", dec)
