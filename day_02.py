# Tip Calculator

# Greeting
print("Welcome to the Tip Calculator")

# Bill
bill = float(input("What was the total bill? "))

# Tip
tip = float(input("What percentage tip would you like to give? "))

# Number of people
num_of_people = float(input("How many peaople to split the bill? "))

# Result
split_bill = round((bill + (tip / 100 * bill))/num_of_people, 2)

print(f'Each person should pay: ${split_bill}')