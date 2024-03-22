# Accessing the content of the starting letter
with open("./Input/Letters/starting_letter.txt") as data:
    letter = data.read()

# Accessing the list of names
with open("./Input/Names/invited_names.txt") as data:
    names = data.readlines()

# Iterating through each name in the list
for name in names:
    # Removing newline characters from each name
    stripped_name = name.strip("\n")

    # Replacing placeholder [name] in the letter with the current name
    new_letter = letter.replace("[name]", stripped_name)

    # Creating a new letter file for each name in the output directory
    # The file name is based on the original name with "_letter.txt" appended
    with open(f"./Output/ReadyToSend/{stripped_name}_letter.txt", mode="w") as named_letter:
        # Writing the personalized letter to the new file
        named_letter.write(new_letter)
