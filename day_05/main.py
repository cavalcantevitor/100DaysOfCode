# Password Generator
import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
symbols = "!@#$%^&*()_+-={}[]|:;<>,.?`"
numbers = "0123456789"

password = ""

print("Welcome to the password generator")

num_of_letters = int(input("How many letters would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like? "))
num_of_numbers = int(input("How many numbers would you like? "))

# Characters not randomized - NOT SO STRONG PASSWORD

# for letter in range(1, num_of_letters + 1):
#     random_number = random.randint(0, 51)
#     password += letters[random_number]

# for symbol in range(1, num_of_symbols + 1):
#     random_number = random.randint(0, 26)
#     password += symbols[random_number]

# for letter in range(1, num_of_numbers + 1):
#     random_number = random.randint(0, 9)
#     password += numbers[random_number]

# Characters randomized - STRONGER PASSWORD

password_list = []

for letter in range(1, num_of_letters + 1):
    random_number = random.randint(0, 51)
    password_list.append(letters[random_number])

for symbol in range(1, num_of_symbols + 1):
    random_number = random.randint(0, 26)
    password_list.append(symbols[random_number])

for letter in range(1, num_of_numbers + 1):
    random_number = random.randint(0, 9)
    password_list.append(numbers[random_number])

random.shuffle(password_list)

for char in password_list:
    password += char

print(password)