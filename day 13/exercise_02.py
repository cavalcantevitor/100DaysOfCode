# Debugging Exercise 2

# Which year do you want to check?

# year = input() -> There was a bug here
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  