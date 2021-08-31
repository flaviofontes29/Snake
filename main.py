from turtle import Screen, Turtle
import time
from snaker import Snaker
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snaker = Snaker()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snaker.up, "Up")
screen.onkey(snaker.down, "Down")
screen.onkey(snaker.left, "Left")
screen.onkey(snaker.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snaker.move()
    # Detect collision with food
    if snaker.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snaker.extend()
    # Detect collision with wall
    if (
        snaker.head.xcor() > 290
        or snaker.head.xcor() < -290
        or snaker.head.ycor() > 290
        or snaker.head.ycor() < -290
    ):
        snaker.reset()
        scoreboard.reset()
    # Detect collision  with  tail
    for segment in snaker.segments[1:]:
        if segment == snaker.head:
            pass
        elif snaker.head.distance(segment) < 10:
            snaker.reset()
            scoreboard.reset()
