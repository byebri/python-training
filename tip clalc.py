print("welcome to my tip calc")
cost = input("whats the damage?\n$ ")
percent = input("what percent tip?\n% ")
split = input("split how many ways?\n")
percent1 = int(percent) / 100
tip = int(cost) * percent1
total = tip + int(cost)
x = total / int(split)
print(f"each person pays $ {x}")
