import string

def cesar_cipher(message, key):
    alphabet = string.printable + 'éèêàçùôî'
    encrypted_message = ""
    for char in message:
        index_carac_in_printable = alphabet.index(char)
        index_crypted_char = (index_carac_in_printable + key) % len(alphabet)
        crypted_char = alphabet[index_crypted_char]
        encrypted_message += crypted_char
    return encrypted_message

def cesar_decypher(encrypted_message, key):
    return cesar_cipher(encrypted_message, -key)

def cesar_brute_force(encrypted_message):
    print("*" * 30)
    for shift in range(len(string.printable)):
        print(cesar_decypher(encrypted_message, shift))
    print("*" * 30)

def vigenere_cypher(message, key):
    alphabet = string.printable + 'éèêàçùôî'
    encrypted_message = ""
    for index in range(len(message)):
        encrypted_message += cesar_cipher(message[index], alphabet.index(key[index % len(key)]))
    return encrypted_message

def vigenere_decypher(encrypted_message, key):
    alphabet = string.printable + 'éèêàçùôî'
    decrypted_message = ""
    for index in range(len(encrypted_message)):
        decrypted_message += cesar_decypher(encrypted_message[index], alphabet.index(key[index % len(key)]))
    return decrypted_message

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the encryption key: "))
    encrypted_text = cesar_cipher(text, shift)
    print(f"Encrypted text: {encrypted_text}")
    print("Brute force:")
    cesar_brute_force(encrypted_text)
    vigenere_key = input("Enter the Vigenère encryption key: ")
    print("Vigenère encryption:")
    print(vigenere_cypher(text, vigenere_key))
    print("Vigenère decryption:")
    print(vigenere_decypher(encrypted_text, vigenere_key))