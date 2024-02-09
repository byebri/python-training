import random
choices = ["rock", "paper", "scissors"]
bot = random.randint(0, len(choices) - 1)
bots_choice = choices[bot]

p_choice = input("let's play a game, choose rock, paper or scissors\n").lower()
choice_index = choices.index(p_choice)
print("lets see if you win...")

print("player's choice...", p_choice)
print("bot's choice...", bots_choice)
if bot == 0 and choice_index == 0:
    print("draw")
elif bot == 1 and choice_index == 1:
    print("draw")
elif bot == 2 and choice_index == 2:
    print("draw")
elif bot == 0 and choice_index == 1:
    print("u win")
elif bot == 1 and choice_index == 0:
    print("u lose")
elif bot == 2 and choice_index == 1:
    print("u lose")
elif bot == 0 and choice_index == 2:
    print("u lose")
elif bot == 1 and choice_index == 2:
    print("u win")
elif bot == 2 and choice_index == 0:
    print("u win")
