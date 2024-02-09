print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
name1l = name1.lower()
name2l = name2.lower()

t = name1l.count("t") + name1l.count("r") + name1l.count("u") + name1l.count("e") + name2l.count("t") + name2l.count("r") + name2l.count("u") + name2l.count("e")

l = name1l.count("l") + name1l.count("o") + name1l.count("v") + name1l.count("e") + name2l.count("l") + name2l.count("o") + name2l.count("v") + name2l.count("e")


final_result = t*10 + l

if final_result <=10 or final_result >= 90:
    print(f"Your score is {final_result}, you go together like coke and mentos.")
elif final_result >= 40 and final_result <= 50:
    print(f"Your score is {final_result}, you are alright together.")
else:
    print(f"Your score is {final_result}.")
