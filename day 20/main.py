# Import necessary modules
from turtle import Screen
from snake import Snake
import time

# Set up the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off automatic screen updates

# Create a Snake object
snake = Snake()

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

# Close the game window when clicked
screen.exitonclick()
