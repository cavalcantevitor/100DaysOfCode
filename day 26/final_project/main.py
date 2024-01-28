import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format:
# example = {"A": "Alfa", "B": "Bravo"}

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alphabet)

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}
# print(nato_dict)

# 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type a word: ")
nato_word = [nato_dict.get(letter.upper()) for letter in user_input]
print(nato_word)