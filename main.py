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


# i = 0
# for turtle_snake in range(0, 3):
#     turtle = Turtle(shape = "square")
#     turtle.color("white")
#     turtle.penup()
#     turtle.goto(x=i, y=0)
#     i-=20   

#for_lopp_v2
#creating positions in the separated tuples placed in the list
# starting_positions = [(0,0), (-20,0), (-40, 0)]
# segments = []

# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

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

        #game_is_on = False
        #score.game_over()

        # to reset the score to the highest score
        score.reset()
        snake.reset_snake()
        

    #DEtect collision with tail
    #if head collids with any segment in the tail:
        #trigger game_over
    #v1    
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
        # elif snake.head.distance(segment) < 10:
        #     game_is_on = False
        #     score.game_over()

    #v2
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            #game_is_on = False
            #score.game_over()
            score.reset()
            snake.reset_snake()


        
        

    # for seg_num in range(len(segments)-1, 0, -1):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()               
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)
    
        
screen.exitonclick()