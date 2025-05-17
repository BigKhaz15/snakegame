from turtle import Screen
import time

screen = Screen()
screen.tracer(0)

def screen_setup():
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Adam's Snake Game")


from snake import Snake
from food import Food
from scoreboard import Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()


def restart_game():
    snake.reset()
    scoreboard.reset_scoreboard()
    food.reset()
    play_game()
    screen.update()

def play_game():
    screen_setup()

    screen.listen()
    screen.onkey(fun= snake.up, key="Up")
    screen.onkey(fun= snake.down, key="Down")
    screen.onkey(fun= snake.left, key="Left")
    screen.onkey(fun= snake.right, key="Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        snake.move()
        #Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.update_score()

        #Detect collision with wall
        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()
            time.sleep(.65)

        #Detect collision with tail
        for segment in snake.snake_segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()
                time.sleep(.65)
screen.listen()
screen.onkey(restart_game, "r")
play_game()
screen.mainloop()




