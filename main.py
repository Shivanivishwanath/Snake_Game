from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

mypen = Turtle()
mypen.penup()
mypen.setposition(280,-280)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
# mypen.hideturtle()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#Movement of snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food)<20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    #Detect collision with wall

    if snake.head.xcor()>280 or snake.head.xcor()<-288 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[:0:-1]:
        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()
