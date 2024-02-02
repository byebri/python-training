import random
import hangman_art
from hangman_words import word_list
chosen = random.choice(word_list)
end_of_game = False
print(hangman_art.logo)
list_empty = []
for x in range(len(chosen)):
    list_empty.append("_")
list_to_str = ' '.join(list_empty)
print(list_to_str)
lives = 6
guessed_letters = []
while not end_of_game:
    guess_letter = input("guess a letter\n").lower()
    guessed_letters.append(guess_letter)
    for position in range(len(chosen)):
        letter_num = chosen[position]
        if letter_num == guess_letter:
            list_empty[position] = letter_num
    if guess_letter not in list_empty:
        lives -= 1
        print(f"{hangman_art.stages[lives]}Lives remaining: {lives}")
    print(' '.join(list_empty))
    print("you have guessed " + ' '.join(guessed_letters))

    if "_" not in list_empty:
        print("you win")
        end_of_game = True
        exit()
    elif lives == 0:
        print("it was " + chosen)
        print("you lose")
        exit()
