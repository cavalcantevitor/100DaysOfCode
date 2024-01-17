# Higher Lower Game

import art
print(art.logo)

import game_data
import random

def random_number():
    # Generate a random index within the range of available data
    number = random.randint(0, len(game_data.data) - 1)
    return number

def generate_item():
    # Generate a random celebrity item for comparison
    item = game_data.data[random_number()]
    return item

def compare_result(item_a, item_b):
    # Compare follower counts of two items and determine the correct answer
    if item_a["follower_count"] > item_b["follower_count"]:
        return "A"
    elif item_a["follower_count"] < item_b["follower_count"]:
        return "B"

def display_comparison(item_a, item_b):
    # Display the comparison between two items, including name, description, country, and follower count
    print(f"Compare A: {item_a['name']}, a {item_a['description']}, from {item_a['country']}")
    print(art.vs)
    print(f"Against B: {item_b['name']}, a {item_b['description']}, from {item_b['country']}")

def play_game():
    # Initial setup for the first two items
    item_a = generate_item()
    item_b = generate_item()
    display_comparison(item_a, item_b)
    
    # Get the user's initial guess and the correct answer for the first comparison
    guess = input("Who has more followers? Type 'A' or 'B'? ")
    answer = compare_result(item_a, item_b)

    # Variable to keep track of the player's score
    score = 0

    # Main game loop
    while guess == answer:
        # Update items for the next comparison
        item_a, item_b = item_b, generate_item()
        display_comparison(item_a, item_b)
        
        # Get the user's guess for the current comparison
        guess = input("Who has more followers? Type 'A' or 'B'? ")
        
        # Get the correct answer for the current comparison
        answer = compare_result(item_a, item_b)

        # Increment the score for each correct guess
        score += 1

    # Display final score when the player makes a wrong guess
    print(f"Sorry, that is wrong. Final score: {score}")

# Check if the script is being run as the main program
if __name__ == "__main__":
    play_game()
