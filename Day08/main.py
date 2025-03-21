# Import and print the logo from art.py (assuming you have the art.py module)

import art
print (art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # Ensure the shift is within the bounds of the alphabet (0-25)
    shift_amount = shift_amount % len(alphabet)

    if encode_or_decode == "decode":
        shift_amount *= -1  # Reverse the shift if decoding

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # Ensure it wraps around alphabet
            output_text += alphabet[shifted_position]
        else:
            # Keep the symbol/number/space as is
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Start the Caesar Cipher Program
continue_code = True

while continue_code:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Call the caesar cipher function with the user's input
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        continue_code = False
        print("Goodbye!")
