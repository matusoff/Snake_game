from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    #Detect collision with food(method distance --> if snake is close to food at 15 pix or less
    # then food is relocated)
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()

    #Detect collision with wall
    if snake.head.xcor() >290 or snake.head.xcor() < -290 or snake.head.ycor() >290 or snake.head.ycor() < -290:
        # if you want Game Over then 2  lines of code - game_is_on = False 
        # and score.game_over() should be activated

        # to reset the score to the highest score
        score.reset()
        snake.reset_snake()
        

    #DEtect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #score.game_over()
            score.reset()
            snake.reset_snake()
    
        
screen.exitonclick()
