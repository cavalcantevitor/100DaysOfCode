from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():

    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    is_empty = False

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                  f"\nEmail: {username} "
                                                  f"\nPassword: {password} "
                                                  f"\nIs is okay to save?")

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        is_empty = True

    if is_empty:
        messagebox.showinfo(title="Please don't leave any fields empty")
    else:
        if is_ok:
            with open("passwords.txt", "a") as data:
                data.write(f"{website}; ")
                data.write(f"{username}; ")
                data.write(f"{password}\n")

                website_entry.delete(0, "end")
                password_entry.delete(0, "end")

                username_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

# Create the main window
window = Tk()
window.title("MyPass Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2, row=1)

# Website Label
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

# Email/username Label
username_label = Label(text="Email/Username:")
username_label.grid(column=1, row=3)

# Password Label
password_label = Label(text="Password")
password_label.grid(column=1, row=4)

# Website Entry
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2)

# Email/username Entry
username_entry = Entry(width=35)
username_entry.insert(0, "me@email.com")
username_entry.grid(column=2, row=3, columnspan=2)

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

# Generate Password
button = Button(text="Generate Password")
button.grid(column=3, row=4)

# Save Password
button = Button(text="Add", width=36, command=save_password)
button.grid(column=2, row=5, columnspan=2)

window.mainloop()
