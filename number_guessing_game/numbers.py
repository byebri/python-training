import random
import art


def number_guessing():
    guessed_number1 = int(input("Guess a number\n"))
    return guessed_number1


def play_again_func():
    play_again = input("Play again? [y/n]\n").lower()
    if play_again == "n":
        return False
    elif play_again == "y":
        return True
    else:
        print("Invalid input.")


def play_game():
    while True:
        EASY_BOT_CHOICE = random.randint(1, 50)
        HARD_BOT_CHOICE = random.randint(1, 100)

        def hard_mode():
            lives_left = 5
            while lives_left > 0:
                guessed_number1 = number_guessing()
                if guessed_number1 == HARD_BOT_CHOICE:
                    print("Congratulations! You guessed the number correctly!")
                    if play_again_func():
                        return
                elif guessed_number1 < HARD_BOT_CHOICE:
                    print("The number is too low")
                    lives_left -= 1
                    print(f"Lives left: {lives_left}")
                elif guessed_number1 > HARD_BOT_CHOICE:
                    print("The number is too high")
                    lives_left -= 1
                    print(f"Lives left: {lives_left}")
                else:
                    lives_left -= 1
                    print(f"Wrong guess! Lives left: {lives_left}")
            print("Game over! You lose.")
            if play_again_func():
                return

        def easy_mode():
            lives_left = 10
            while lives_left > 0:
                guessed_number1 = number_guessing()
                if guessed_number1 == EASY_BOT_CHOICE:
                    print("Congratulations! You guessed the number correctly!")
                    if play_again_func():
                        return
                elif guessed_number1 < EASY_BOT_CHOICE:
                    print("The number is too low")
                    lives_left -= 1
                    print(f"Lives left: {lives_left}")
                elif guessed_number1 > EASY_BOT_CHOICE:
                    print("The number is too high")
                    lives_left -= 1
                    print(f"Lives left: {lives_left}")
                else:
                    lives_left -= 1
                    print(f"Wrong guess! Lives left: {lives_left}")
            print("Game over! You lose.")
            if play_again_func():
                return

        print("Welcome\nI'm thinking of a number...")
        game_mode = input("Do you want to play Easy mode or Hard mode? [e/h]\n")
        if game_mode == "e":
            print("In easy mode, you get 10 lives and the number ranges from 1-50")
            easy_mode()
        elif game_mode == "h":
            print("In hard mode, you get 5 lives and the number ranges from 1-100")
            hard_mode()
        else:
            print("Invalid input")

        del EASY_BOT_CHOICE
        del HARD_BOT_CHOICE


print(art.logo)
play_game()
