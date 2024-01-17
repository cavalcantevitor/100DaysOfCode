# Debugging Exercise 3

target = int(input())
for number in range(1, target + 1):
  
# if number % 3 == 0 or number % 5 == 0: -> There was a bug here
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")

# if number % 3 == 0: -> There was a bug here
  elif number % 3 == 0:
    print("Fizz")

# if number % 3 == 0: -> There was a bug here
  elif number % 5 == 0:
    print("Buzz")
  else:
    # print([number]) -> There was a bug here
    print(number)