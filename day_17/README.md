# Quiz App

This Python script is a simple quiz application that allows users to test their knowledge on a variety of topics. The quiz questions are stored in the `question_data` module, and the script utilizes the `Question` class to represent each question. The `QuizBrain` class manages the quiz flow, keeping track of the user's score and progress.

## How it Works

1. The script imports the `Question` class, loads question data from the `question_data` module, and creates a list of `Question` objects to form the question bank.

2. The `QuizBrain` class is employed to conduct the quiz. It iterates through the questions, presents them to the user, and keeps track of the score.

3. The user is prompted with questions one by one until there are no more questions left.

4. After completing the quiz, the script prints a congratulatory message and displays the user's final score.
