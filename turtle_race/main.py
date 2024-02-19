import random
from turtle import Turtle, Screen

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
screen.colormode(255)
guess = screen.textinput(title="r,g,b,p,o,y,b", prompt="Guess a colour").lower()
colours = ["red", "green", "blue", "purple", "orange", "yellow", "black"]
y_axis = [0, 50, 100, 150, -50, -100, -150]
all_turtles = []

for turtle_index in range(0, 7):
    tim = Turtle("turtle")
    tim.penup()
    tim.speed(0)
    tim.color(colours[turtle_index])
    tim.goto(x=-230, y=y_axis[turtle_index])
    all_turtles.append(tim)


if guess:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() < 230:
            turtle.forward(random.randint(0, 10))
        else:
            winner = turtle.color()[0]
            race_on = False
            if winner == guess:
                turtle.home()
                winner_message = f"The winner is {guess}!"
                turtle.write(winner_message, True, align="center", font=("Arial", 10, "normal"))
            else:
                turtle.home()
                winner_message = f"The winner is {winner}!\nSorry, {guess} didn't win."
                turtle.write(winner_message, True,  align="center", font=("Arial", 10, "normal"))


screen.exitonclick()
