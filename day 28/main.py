# Pomodoro Clock

# Import required modules
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #

# Define color constants and other constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# Function to reset the timer and other related variables
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    reps = 0
    title_label.config(text="Work", fg=GREEN)
    marks = ""
    check_marks.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- #

# Function to start the timer based on work, short break, or long break
def start_timer():
    global reps
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    reps += 1

    # Check if it's time for a long break, short break, or work session
    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_seconds)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# Function to handle the countdown mechanism
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    # Format seconds with leading zero if less than 10
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    # Update the timer display on the canvas
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    # If count is greater than 0, continue countdown; otherwise, start a new timer
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)

        # Display checkmarks for completed work sessions
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title_label = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 40, "bold"), fg=GREEN)
title_label.grid(column=2, row=1)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Start Button
button = Button(text="Start", command=start_timer)
button.grid(column=1, row=3)

# Reset Button
button = Button(text="Reset", command=reset_timer)
button.grid(column=3, row=3)

# Checkmark
check_marks = Label(text="", bg=YELLOW, fg=GREEN)
check_marks.grid(column=2, row=4)

# Run the main event loop
window.mainloop()