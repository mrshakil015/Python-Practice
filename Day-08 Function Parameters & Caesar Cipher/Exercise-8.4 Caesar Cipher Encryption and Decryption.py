alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to 'encrypt', type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift_number = int(input("Type the shift number: "))

if direction == "encode":
    def encrypt(text, shift_number):
        cipher_text = ""
        for letter in text:
            if letter in alphabet:
                letter_pos = alphabet.index(letter)
                new_pos = (letter_pos + shift_number) % len(alphabet)
                new_letter = alphabet[new_pos]
                cipher_text += new_letter
            else:
                cipher_text += letter  # Add non-alphabetic characters as is
        print(f"The encoded text is {cipher_text}")
    encrypt(text, shift_number)
elif direction == "decode":
    def decrypt(text, shift_number):
        plain_text = ""
        for letter in text:
            if letter in alphabet:
                letter_pos = alphabet.index(letter)
                new_pos = (letter_pos - shift_number) % len(alphabet)
                new_letter = alphabet[new_pos]
                plain_text += new_letter
            else:
                plain_text += letter  # Add non-alphabetic characters as is
        print(f"The decoded text is {plain_text}")
    decrypt(text, shift_number)
