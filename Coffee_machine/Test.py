from menu import MENU
from menu import resources


def play_game():
    while True:
        def coffee_choice_func():
            coffee_choice = input("What would you like? espresso/latte/cappuccino: ").lower()
            if coffee_choice == "r":
                for item, amount in resources.items():
                    if item == "money":
                        print(item.capitalize() + ":", "$" + str(amount))
                    else:
                        print(item.capitalize() + ":", amount)
                play_game()

            elif coffee_choice == "off":
                print("Goodbye!")
                exit()

            elif coffee_choice in ["espresso", "latte", "cappuccino"]:
                coffee = MENU[coffee_choice]
                print("It costs: $", coffee['cost'] / 100)  # Convert cents to dollars for display
                return coffee
            else:
                print("Invalid input")
                exit()

        def check_resource(ingredients):
            if ingredients is None:
                return False
            for item, amount in ingredients.items():
                if resources[item] < amount:
                    print(f"Sorry there is not enough {item}.")
                    return False
            return True

        def coinz():
            print("Please insert coins")
            loonie = int(input("How many loonies: ")) * 100
            quarter = int(input("How many quarters: ")) * 25
            dime = int(input("How many dimes: ")) * 10
            nickel = int(input("How many nickels: ")) * 5
            total_cents = loonie + quarter + dime + nickel
            return total_cents

        def subtract_resources(coffee_choice):
            if coffee_choice:
                for item, amount in coffee_choice['ingredients'].items():
                    resources[item] -= amount

        def add_money(coffee_choice):
            if coffee_choice:
                resources['money'] += coffee_choice['cost']

        coffee_choice = coffee_choice_func()
        if coffee_choice:
            if not check_resource(coffee_choice['ingredients']):
                print("Cannot buy the coffee. Insufficient resources.")
                exit()
            tt_cents = coinz()
            if tt_cents < coffee_choice['cost']:
                print("Cannot buy the coffee. Insufficient funds.")
                exit()
            else:
                change = tt_cents - coffee_choice['cost']
                print(f"Here is your change: ${change / 100}")  # Convert cents to dollars for display
                subtract_resources(coffee_choice)
                add_money(coffee_choice)
        else:
            exit()

        play_again = play_again_func()
        if not play_again:
            print("Goodbye!")
            exit()


def play_again_func():
    play_again = input("Buy more? (y/n)\n").lower()
    if play_again == "n":
        return False
    elif play_again == "y":
        return True
    else:
        print("Invalid input.")
        return play_again_func()


play_game()
