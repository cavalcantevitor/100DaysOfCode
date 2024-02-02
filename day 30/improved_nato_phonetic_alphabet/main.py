import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# example = {"A": "Alfa", "B": "Bravo"}
nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}


# 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_nato_word():
    user_input = input("Type a word: ").upper()
    try:
        nato_word = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, please type only letters")
        generate_nato_word()
    else:
        print(nato_word)


generate_nato_word()
