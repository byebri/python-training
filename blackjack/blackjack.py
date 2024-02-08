import random
import logo
print(logo.logo_1)
read_rules = input("Do you want to read the rules? (y/n):\n")
if read_rules == "y":
    print(logo.rules)
else:
    print("Have fun!\n\n\n")
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

players_random = []
dealers_random = []


def dealer():
    for _ in range(2):
        dealers_random.append(random.choice(cards))


def player():
    for _ in range(2):
        players_random.append(random.choice(cards))


def player_add_more():
    players_random.append(random.choice(cards))


def dealer_add_more():
    while sum(dealers_random) < 17:
        dealers_random.append(random.choice(cards))


def calculate_total(hand):
    total = sum(hand)
    if total >= 21 and 11 in hand:
        total -= 10
    return total


def play_game():
    players_random.clear()
    dealers_random.clear()
    player()
    dealer()

    print("Player's cards:", players_random)
    player_total_1 = sum(players_random[:2])
    if player_total_1 >= 21:
        player_total_1 = calculate_total(players_random[:2])
    print("Player's total:", player_total_1)

    add_more = input("Hit or Stand [h/s]\n").lower()

    dealer_total_2 = None

    if add_more == "h":
        player_add_more()
        print("Player's cards:", players_random)
        player_total = sum(players_random)
        print("Player's total:", player_total)
        if player_total > 21:
            print("Bust. You lose.")
            return play_again_func()

        dealer_add_more()
        dealer_total_2 = sum(dealers_random)
        print("Dealer's cards:", dealers_random[:2])
        print("Dealer's total:", dealer_total_2)
        if dealer_total_2 > 21:
            print("Dealer bust")
            return play_again_func()

        add_more_more = input("Hit or Stand [h/s]\n").lower()
        if add_more_more == "h":
            player_add_more()
            print("Player's cards: ", players_random)
            player_total_add_add = sum(players_random)
            print("Player's total:", player_total_add_add)
            if player_total_add_add > 21:
                print("Bust. You lose.")
                return play_again_func()
            if player_total_add_add == dealer_total_2:
                print("It's a draw")
            elif player_total_add_add > dealer_total_2:
                print("You win")
            else:
                print("You lose")
        elif add_more_more == "s":
            if player_total > dealer_total_2:
                print("You win")
            elif player_total == dealer_total_2:
                print("It's a draw")
            else:
                print("You lose")
            return play_again_func()

    elif add_more == "s":
        print("Player's cards: ", players_random)
        print("Player's total:", player_total_1)

        dealer_add_more()
        dealer_total_2 = sum(dealers_random)
        print("Dealer's cards:", dealers_random)
        print("Dealer's total:", dealer_total_2)

        if dealer_total_2 > 21:
            print("Dealer bust")
        elif player_total_1 > dealer_total_2:
            print("You win")
        elif player_total_1 == dealer_total_2:
            print("It's a draw")
        else:
            print("You lose")
        return play_again_func()

    else:
        print("Invalid input.")


def play_again_func():
    play_again = input("Play again? (y/n)\n").lower()
    if play_again == "n":
        return False
    elif play_again == "y":
        return True
    else:
        print("Invalid input.")


play_play = True
while play_play:
    play_play = play_game()
