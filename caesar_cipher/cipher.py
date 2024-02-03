alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(start_text, start_amount, start_direction):
    end_text = ""
    if start_direction == "decode":
        start_amount *= -1
    for letters in start_text:
        if letters in alphabet:
            position = alphabet.index(letters)
            new_pos = (position + start_amount) % 26
            end_text += alphabet[new_pos]
        else:
            end_text += letters
    print(f"text is {end_text}")


play_again = "yes"
while play_again == "yes":
    from art_for_cipher import logo

    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, start_amount=shift, start_direction=direction)
    play_again = input("start again? [yes/no] ")
