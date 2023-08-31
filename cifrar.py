import sys

def encrypt_cesar(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    if len(sys.argv) != 3:
        print("Usage: python cesar_cipher.py <word> <key>")
        return

    word = sys.argv[1]
    key = int(sys.argv[2])

    encrypted_word = encrypt_cesar(word, key)
    print("Encrypted word:", encrypted_word)

if __name__ == "__main__":
    main()

