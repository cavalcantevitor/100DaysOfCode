from tkinter import *

window = Tk()
window.title("First GUI application")
window.minsize(width=500, height=300)

# Label
label = Label(text="Label")
label.grid(column=0, row=0)


# Button
def button_clicked():
    label.config(text=f"{my_input.get()}")


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=3, row=0)


# Input
my_input = Entry(width=10)
my_input.button = Button(text="Click Me", command=button_clicked)
my_input.grid(column=4, row=3)

window.mainloop()
