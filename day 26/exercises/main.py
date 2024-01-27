# ----- List Comprehension -----
import pandas

numbers = [1, 2, 3]
# print(numbers)

# new_list = [new_item for item in list]
numbers_list = [n + 1 for n in numbers]
# print(numbers_list)

name = "Angela"
letters_list = [letter for letter in name]
# print(letters_list)

range_list = [n * 2 for n in range(1, 5)]
# print(range_list)

# List Comprehension with Conditionals
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
# print(short_names)

long_names_with_caps = [name.upper() for name in names if len(name) >= 5]
# print(long_names_with_caps)

# ----- Dictionary Comprehension -----
import random

# new_dict = {new_key:new_value for item in list if test}

# Dictionary comprehension to create a dictionary with random scores for each student
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# Dictionary comprehension to filter and create a new dictionary with students who passed
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# ----- Looping Through a Pandas Data Frame -----

import pandas

students_df = pandas.DataFrame(student_scores)

for (index, row) in students_df.iterrows():
    print(index, row)