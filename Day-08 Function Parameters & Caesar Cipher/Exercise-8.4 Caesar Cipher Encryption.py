alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to 'encrypt', type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift_number = int(input("Type the shift number: "))

def encrypt(text, shift_number):
    cipher_text=""
    for letter in text:
        letter_pos = alphabet.index(letter)
        new_pos = letter_pos + shift_number
        new_letter = alphabet[new_pos]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
encrypt(text, shift_number)
