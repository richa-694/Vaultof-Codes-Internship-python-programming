def encode_message(message, shift):
    """
    Encode a message by shifting each letter by the given shift number.

    :param message: The message to encode
    :param shift: The shift number
    :return: The encoded message
    """
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            ascii_offset = 65 if char.isupper() else 97  # ASCII offset for uppercase and lowercase letters
            encoded_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encoded_message += encoded_char
        else:
            encoded_message += char  # Leave non-letter characters unchanged
    return encoded_message

def decode_message(message, shift):
    """
    Decode a message by shifting each letter back by the given shift number.

    :param message: The message to decode
    :param shift: The shift number
    :return: The decoded message
    """
    return encode_message(message, -shift)  # Simply call encode_message with a negative shift

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