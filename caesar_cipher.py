def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    # Decrypting is just encrypting with negative shift
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    print("Do you want to encrypt or decrypt?")
    choice = input("Type 'e' for encrypt or 'd' for decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please run the program again.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift. Please use an integer.")
        return

    if choice == 'e':
        result = encrypt(message, shift)
        print(f"\nEncrypted message: {result}")
    else:
        result = decrypt(message, shift)
        print(f"\nDecrypted message: {result}")

if __name__ == "__main__":
    main()
