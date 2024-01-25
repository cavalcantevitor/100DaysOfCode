# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# Create a Snake object
snake = Snake()

# Create a Food object
food = Food()

# Create a Score object
scoreboard = Scoreboard()

# Set up key listeners for snake movement
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Flag to control the game state
game_is_on = True

# Main game loop
while game_is_on:
    screen.update()  # Update the screen manually to reduce flickering
    time.sleep(0.1)  # Add a small delay to control the speed of the game
    snake.move()  # Move the snake

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Close the game window when clicked
screen.exitonclick()
