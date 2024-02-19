import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()

screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.front.distance(food) < 15:
        score.score_up()
        food.refresh()
        snake.extend()

    if snake.front.ycor() > 290 or snake.front.ycor() < -290 or snake.front.xcor() > 290 or snake.front.xcor() < -290:
        game_on = False
        score.game_over()

    for segments in snake.all_snakes[1:]:
        if snake.front.distance(segments) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
