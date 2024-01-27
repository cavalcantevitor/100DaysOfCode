# NATO Phonetic Alphabet Converter

This Python script converts a word into its corresponding NATO phonetic alphabet representation. It uses a CSV file containing the NATO alphabet mapping for each letter.

## Usage

1. **Dictionary Creation:**
The script reads the NATO phonetic alphabet mapping from a CSV file (`nato_phonetic_alphabet.csv`) and creates a dictionary in the format `{"A": "Alfa", "B": "Bravo", ...}`.

    ```python
    import pandas as pd
    
    # Create a dictionary from the CSV file
    nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
    nato_dict = {row.letter: row.code for (_, row) in nato_alphabet.iterrows()}
    print(nato_dict)
    ```

2. **Word to NATO Phonetic Alphabet:**
The user can input a word, and the script will output a list of corresponding NATO phonetic alphabet words.

```python
user_input = input("Type a word: ")
nato_word = [nato_dict.get(letter.upper()) for letter in user_input]
print(nato_word)
```