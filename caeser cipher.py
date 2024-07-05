def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            if char.isupper():
                result += alphabet[(alphabet.index(char.lower()) + shift) % len(alphabet)].upper()
            else:
                result += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        else:
            result += char
    if encrypt:
        print(f"Encrypted message: {result}")
    else:
        print(f"Decrypted message: {result}")

def main():
    while True:
        choice = input("Enter 'e' to encrypt or 'd' to decrypt (or 'q' to quit): ")
        if choice == 'q':
            break
        elif choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (1-26): "))
            caesar_cipher(message, shift, encrypt=True)
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (1-26): "))
            caesar_cipher(message, shift, encrypt=False)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
