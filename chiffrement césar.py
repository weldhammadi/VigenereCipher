import string

def caesar_cipher(text, shift):
    encrypted_text = ""
    shift = shift % 26
    text = text.lower()
    for letter in text:
        if letter in string.ascii_lowercase:
            letter = chr(ord(letter) + shift)
            if ord(letter) > 122:
                letter = chr(ord(letter) - 26)
            if ord(letter) < 97:
                letter = chr(ord(letter) + 26)
        encrypted_text += letter

    return encrypted_text

def brute_force(text):
    for i in range(26):
        encrypted_text = caesar_cipher(text, -i)
        print(f"i = {i} {encrypted_text}")

    return encrypted_text

def vigenere_cipher(text, key):
    encrypted_text = ""
    for i in range(len(text)):
        shift = ord(key[i % len(key)]) % 26
        
        encrypted_text += caesar_cipher(text[i], shift)

    return encrypted_text

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the encryption key: "))
    encrypted_text = caesar_cipher(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    print("Brute force:")
    brute_force(encrypted_text)
    print("Vigenère encryption:")
    print(vigenere_cipher(text, "rdhvysk"))
