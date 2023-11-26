from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)
should_continue = True


def shift_alphabet(shift_amount):
    alphabet_len = len(alphabet)
    if shift_amount > alphabet_len:
        shift_amount = shift_amount % alphabet_len
    shifted_items = alphabet[:shift_amount]
    rest_items = alphabet[shift_amount:]
    shifted_list = rest_items + shifted_items
    return shifted_list


def caesar_cipher(plain_text, shift_amount, cipher_direction):
    print(cipher_direction)
    if cipher_direction != 'encode' and cipher_direction != 'decode':
        print("You can only use 'encode' or 'decode' keywords")
        return

    shifted_alphabet = shift_alphabet(shift_amount)
    output_text = ''

    for char in plain_text:
        if char in shifted_alphabet:
            if cipher_direction == 'encode':
                idx = alphabet.index(char)
                output_text += shifted_alphabet[idx]
            elif cipher_direction == 'decode':
                idx = shifted_alphabet.index(char)
                output_text += alphabet[idx]
        else:
            output_text += char

    print(f"The {cipher_direction}d text is {output_text}")


while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar_cipher(plain_text=text, shift_amount=shift, cipher_direction=direction)

    result = input("Type 'yes' if you want to do it again. Otherwise type 'no'").lower()
    if result != 'yes':
        should_continue = False
        print("Goodbye")
