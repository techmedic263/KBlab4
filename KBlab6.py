# Vigenère Cipher Implementation

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyword = "IHATEPEOPLE"

def letter_to_index(letter, alphabet):
    return alphabet.index(letter.upper())

def index_to_letter(index, alphabet):
    return alphabet[index % len(alphabet)]

def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plain_index = letter_to_index(plaintext_letter, alphabet)
    cipher_index = (plain_index + key_index) % len(alphabet)
    return index_to_letter(cipher_index, alphabet)

def undo_vigenere_index(key_letter, cipher_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    cipher_index = letter_to_index(cipher_letter, alphabet)
    plain_index = (cipher_index - key_index) % len(alphabet)
    return index_to_letter(plain_index, alphabet)

def encrypt_vigenere(key, plaintext, alphabet):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char in alphabet:
            cipher_char = vigenere_index(key[key_index % len(key)], char, alphabet)
            ciphertext += cipher_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(key, ciphertext, alphabet):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char in alphabet:
            plain_char = undo_vigenere_index(key[key_index % len(key)], char, alphabet)
            plaintext += plain_char
            key_index += 1
        else:
            plaintext += char
    return plaintext

def vigenere_sq(alphabet):
    size = len(alphabet)
    print("Vigenère Square:")
    for i in range(size):
        row = ""
        for j in range(size):
            row += f"{alphabet[(i+j)%size]} "
        print(row.strip())

def main():
    while True:
        print("\nVigenère Cipher Menu")
        print("1) Encrypt")
        print("2) Decrypt")
        print("3) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            plaintext = input("Enter plain text: ")
            encrypted = encrypt_vigenere(keyword, plaintext, alphabet)
            print(f"Encrypted text: {encrypted}")
        elif choice == "2":
            ciphertext = input("Enter cipher text: ")
            decrypted = decrypt_vigenere(keyword, ciphertext, alphabet)
            print(f"Decrypted text: {decrypted}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()
