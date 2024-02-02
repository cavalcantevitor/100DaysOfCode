from tkinter import *
import pandas
import random

# *---------- READING DATA ----------*
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# *---------- CREATING NEW FLASH CARDS ----------*
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_img, image=front_card_img)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


# *---------- CREATING NEW FLASH CARDS ----------*

def flip_card():
    canvas.itemconfig(card_img, image=back_card_img)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")


# *---------- IS KNOWN ----------*

def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


# *---------- UI SETUP ----------*

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

# Create the main window
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
card_img = canvas.create_image(400, 263, image=front_card_img)
title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word = canvas.create_text(400, 263, text="", font=WORD_FONT)
canvas.grid(column=1, row=1, columnspan=2)

# Green Button
green_button_image = PhotoImage(file="images/right.png")
green_button = Button(image=green_button_image, highlightthickness=0, bd=0, command=is_known)
green_button.grid(column=1, row=2)

# Red Button
red_button_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=red_button_image, highlightthickness=0, bd=0, command=next_card)
red_button.grid(column=2, row=2)

next_card()

window.mainloop()
