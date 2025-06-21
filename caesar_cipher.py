# Simple Caesar Cipher in Python

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Keep case (upper or lower)
            base = ord('A') if char.isupper() else ord('a')
            # Shift and wrap around alphabet using modulo
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Leave non-letters unchanged
            result += char
    return result

def decrypt(text, shift):
    # Decryption is just shifting in the opposite direction
    return encrypt(text, -shift)

def main():
    # User inputs
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (integer): "))

    # Encrypt and decrypt
    encrypted = encrypt(message, shift)
    decrypted = decrypt(encrypted, shift)

    print(f"\nEncrypted: {encrypted}")
    print(f"Decrypted (to verify): {decrypted}")

if __name__ == "__main__":
    main()
