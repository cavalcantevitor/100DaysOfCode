# Guessing game

# Printing ASCII art
import art
print(art.logo)

# Greeting
print("Welcome to the Guessing Game")
print('I am thinking a number between 1 and 100')

# Creating random number
import random
random_number = random.randint(1, 100)

# Choose level difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == 'easy':
    attempts = 10
    print(f"You have {attempts} remaining to guess the number")
elif difficulty == 'hard':
    attempts = 5
    print(f"You have {attempts} remaining to guess the number")

# Verifying attempt
while attempts != 0:

    # Making an attempt
    guess = int(input("Make a guess: "))

    if guess != random_number:
        attempts -= 1
        if random_number > guess:
            print("Too low")
        elif random_number < guess:
            print("Too high")
        print("Guess again")
        print(f"You have {attempts} attempts left")
    else:
        break

if guess == random_number:
    print("You won!")
else:
    print(f"You ran out of attempts, you lost. The answer was: {random_number}")
