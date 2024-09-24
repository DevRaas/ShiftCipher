def caesar_cipher(message, shift, mode="encrypt"):
    if mode == "decrypt":
        shift = -shift
    shift = shift % 26
    
    result = ""
    for char in message:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char
    
    return result

def main():
    print("ShiftCipher: Caesar Cipher Tool")
    option = input("Choose an option (1-Encrypt, 2-Decrypt): ")

    if option not in ['1', '2']:
        print("Invalid choice. Please select either 1 or 2.")
        return

    message = input("Enter the message: ")

    try:
        shift = int(input("Enter the shift value: "))
        shift = shift % 26
    except ValueError:
        print("Invalid shift value. Please enter a whole number.")
        return

    mode = "encrypt" if option == '1' else "decrypt"
    result = caesar_cipher(message, shift, mode)

    if mode == "encrypt":
        print(f"Encrypted message: {result}")
    else:
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
