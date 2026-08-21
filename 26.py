def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char

    return result
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift_val = int(input("Enter the shift value (e.g., 3): "))
    encrypted = caesar_cipher(message, shift_val, mode="encrypt")
    decrypted = caesar_cipher(encrypted, shift_val, mode="decrypt")
    print("\n--- Results ---")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")