from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Random",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        # Green Button
        self.green_button_image = PhotoImage(file="images/true.png")
        self.green_button = Button(image=self.green_button_image, highlightthickness=0, bd=0, command=self.correct_answer)
        self.green_button.grid(column=1, row=3)

        # Red Button
        self.red_button_image = PhotoImage(file="images/false.png")
        self.red_button = Button(image=self.red_button_image, highlightthickness=0, bd=0, command=self.wrong_answer)
        self.red_button.grid(column=2, row=3)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz')
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")

    def correct_answer(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def wrong_answer(self):
        answer = "False"
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)