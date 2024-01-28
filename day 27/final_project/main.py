from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="0")
# Gets text in entry
print(entry.get())
entry.grid(column=2, row=1)

# Miles
miles = Label(text="Miles")
miles.grid(column=3, row=1)

# is equal to
equal_to = Label(text="is equal to")
equal_to.grid(column=1, row=2)

# User text calculated
user_text = Label(text=f"{entry.get()}")
user_text.grid(column=2, row=2)

# Km
km = Label(text="Km")
km.grid(column=3, row=2)


# Buttons
def action():
    user_text.config(text=f"{round(float(entry.get()) * 1.609)}")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=2, row=3)

window.mainloop()
