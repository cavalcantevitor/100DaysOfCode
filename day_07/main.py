# Hangman

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

hangman_words.word_list

end_of_game = False
lives = 6

# Print game logo
print(hangman_art.logo)

# Create blanks
guesses = []
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(
            f"Your guess was: {guess} and you already tried this letter. Please guess another one next time"
        )

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(
            f"The letter you guessed was : {guess}. Your guess was wrong, you lost a life. You now have {lives} lives"
        )
        if lives == 0:
            end_of_game = True
            print(f"You lost. The word was {chosen_word}")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    if guess in guesses:
        print(
            f"Your guess was: {guess} and you already tried this letter. Please guess another one next time"
        )

    guesses.append(guess)

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])