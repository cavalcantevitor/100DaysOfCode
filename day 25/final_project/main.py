import turtle
import pandas as pd

# Set up the turtle screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the map image
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Create a turtle for drawing
t = turtle.Turtle()

# Read the U.S. states data from CSV
df = pd.read_csv("50_states.csv")
us_states = df.state.to_list()
correct_answers = []

# Loop until all states are guessed or user exits
while len(correct_answers) < 50:

    # Get user input for a U.S. state
    answer = screen.textinput(title=f"{len(correct_answers)}/50", prompt="Type a U.S. state")
    formatted_answer = answer.title()

    # Check if user wants to exit
    if formatted_answer == "Exit":
        # Find missing states and save to CSV
        missing_states = [state for state in us_states if state not in correct_answers]
        new_df = pd.DataFrame(missing_states)
        new_df.to_csv("states_to_learn.csv")
        break

    # Check if the entered state is valid
    if formatted_answer in us_states:
        # Create a turtle for displaying the state name
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # Get the coordinates for the entered state
        x_coord = int(df[df.state == formatted_answer].x)
        y_coord = int(df[df.state == formatted_answer].y)

        # Move the turtle to the state's coordinates and write the state name
        t.goto(x_coord, y_coord)
        t.write(f"{formatted_answer}", align="center")

        # Update the correct_answers list
        correct_answers.append(formatted_answer)
