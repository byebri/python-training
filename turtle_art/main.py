from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
screen = Screen()
tim.speed(0)
screen.colormode(255)
tim.penup()
tim.setpos(-100, -100)
tim.pendown()
colors = colorgram.extract('lol.jpg', 6)


def random_color():
    mylist = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    rando = random.choice(mylist)
    return rando


def moveup():
    tim.penup()
    tim.sety(tim.ycor() + 10)
    tim.setx(-100)
    tim.pendown()


for _ in range(20):
    moveup()
    for _ in range(20):
        tim.pencolor(random_color())
        tim.dot(5)
        tim.penup()
        tim.forward(10)
        tim.pendown()

screen.exitonclick()
