# Secret Code Generator

def encode_message(message, shift):
    """
    Encode a message by shifting each letter by the given shift number.

    The parameter message: The message to be encoded. It is a string.
    The parameter shift: The shift number to be used for encoding, like how much the string should be shifted. It is an integer.

    :return: The encoded message
    """
    encoded_message = ""  # Initializes an empty string to store the encoded message.

    for char in message:  # Iterates over each character in the input message string.
        if char.isalpha():  # Check if the character is a letter (either uppercase or lowercase). If true, proceeds with encoding
            ascii_offset = 65 if char.isupper() else 97
            # Determines the ASCII offset for the current character: Uppercase letters: 65 (ASCII value of 'A') Lowercase letters: 97 (ASCII value of 'a')
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)  # Calculates the encoded character
            encoded_message += encoded_char  # Appends the encoded character to the encoded_message string.
        else:
            encoded_message += char  # If the character is not a letter (like space or symbol), leaves it unchanged and appends it to the encoded_message string.

    return encoded_message  # Returns the fully encoded message

def decode_message(message, shift):
    """
    Decode a message by shifting each letter back by the given shift number.

    :param message: The message to decode
    :param shift: The shift number
    :return: The decoded message
    """
    return encode_message(message, -shift)  # Simply call encode_message with a negative shift.

def handle_user_input():
    """
    Handle user input and menu choices.
    """
    while True:
        print("Secret Code Generator")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            message = input("Enter a message to encode: ")
            shift = int(input("Enter a shift number: "))
            encoded_message = encode_message(message, shift)
            print("Encoded message:", encoded_message)
        elif choice == "2":
            message = input("Enter a message to decode: ")
            shift = int(input("Enter a shift number: "))
            decoded_message = decode_message(message, shift)
            print("Decoded message:", decoded_message)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    handle_user_input()