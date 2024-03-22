# Import necessary modules
from turtle import Turtle, Screen
import random

# Create a screen for the turtle race
screen = Screen()

# Get user's bet on the winning turtle
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? ")
print(user_bet)

# Set up the screen dimensions
screen.setup(width=500, height=400)

# Define colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create a list to store all turtle objects
all_turtles = []

# Flag to control the race state
is_race_on = False

# Initial y-coordinate for placing turtles
y = -120

# Create turtles with different colors and position them
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)
    y += 40

# If the user has made a bet, start the race
if user_bet:
    is_race_on = True

# Main loop for the turtle race
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # Determine if the user's bet matches the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")

        # Move each turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Close the screen when clicked
screen.exitonclick()
