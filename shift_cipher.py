def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            encrypted_message += char
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    return caesar_cipher_encrypt(encrypted_message, -shift)

def main():
    print("ShiftCipher: Caesar Cipher Tool")
    print("1. Encrypt")
    print("2. Decrypt")
    
    choice = input("Choose an option (1/2): ")
    if choice not in ['1', '2']:
        print("Invalid choice. Please select either 1 or 2.")
        return

    message = input("Enter the message: ")
    
    try:
        shift = int(input("Enter the shift value: "))
        if shift < 0:
            print("Shift value should be non-negative. Using positive equivalent.")
            shift = shift % 26
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == '1':
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == '2':
        decrypted_message = caesar_cipher_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
