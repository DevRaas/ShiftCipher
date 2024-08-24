# ShiftCipher

**ShiftCipher** is a Python tool for encrypting and decrypting text using the Caesar Cipher algorithm. This classic encryption method shifts each letter in the plaintext by a fixed number of places down or up the alphabet.

## Features

- **Encryption**: Convert plaintext to ciphertext using a specified shift value.
- **Decryption**: Convert ciphertext back to plaintext using the same shift value used for encryption.

## Installation

To use **ShiftCipher**, you'll need Python installed on your machine. You can then download or clone the repository to get the script.

### Clone the Repository

```bash
git clone https://github.com/DevRaas/ShiftCipher.git
cd ShiftCipher
```

### Direct Download

Download the `shift_cipher.py` file directly from the [releases](https://github.com/DevRaas/ShiftCipher/releases) section.

## Usage

1. **Run** the script using Python:

    ```bash
    python shift_cipher.py
    ```

2. **Choose** an operation by entering `1` for encryption or `2` for decryption.
3. **Enter** the message and the shift value when prompted.

### Example

#### Encryption

```
Choose an option (1/2): 1
Enter the message: Hello, World!
Enter the shift value: 3
Encrypted message: Khoor, Zruog!
```

#### Decryption

```
Choose an option (1/2): 2
Enter the message: Khoor, Zruog!
Enter the shift value: 3
Decrypted message: Hello, World!
```

## Functions

- `caesar_cipher_encrypt(message, shift)`: Encrypts a given message using the Caesar Cipher with the specified shift value.
- `caesar_cipher_decrypt(encrypted_message, shift)`: Decrypts a given encrypted message using the Caesar Cipher with the specified shift value.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and create a pull request. If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## Contact

For questions or feedback, please contact [roshanajith7911@gmail.com].

## Acknowledgements

- Inspired by classic cryptographic techniques.
- Thanks to the open-source community for the Python libraries and tools used.

