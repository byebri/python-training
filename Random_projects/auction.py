auction_ppl = []


def add_new_person(name, money):
    auction_ppl.append({"name": name, "money": money})


end_bindings = False
while not end_bindings:
    my_name = input("Whats your name?\n")  # Add name
    my_money = int(input("How much do you want to bid?\n$"))  # amount of money
    add_new_person(name=my_name, money=my_money)
    choice = input("add more ppl?? [y/n]\n")
    if choice == "n":
        end_bindings = True


if end_bindings:
    highest_bid = max(auction_ppl, key=lambda employee: employee['money'])
    print(f"The winner is...{highest_bid['name']}\nWith the amount of... ${highest_bid['money']}")