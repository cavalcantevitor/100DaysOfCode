from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
from random import randint, shuffle, choice


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    pswd = "".join(password_list)
    password_entry.insert(0, f"{pswd}")
    pyperclip.copy(pswd)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": username,
        "password": password,
    }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Writing new data
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Writing new data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

        username_entry.focus()


# ---------------------------- SEARCH JSON FILE ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website}", message=f"Email: {data[website]["email"]}\n"
                                                            f"Password: {data[website]["password"]}")
        else:
            messagebox.showinfo(title="Error", message="No details for this website exists")


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
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=2, row=2)

# Email/username Entry
username_entry = Entry(width=35)
username_entry.insert(0, "me@email.com")
username_entry.grid(column=2, row=3, columnspan=2)

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

# Generate Password
button = Button(text="Generate Password", command=generate_password)
button.grid(column=3, row=4)

# Save Password
button = Button(text="Add", width=36, command=save_password)
button.grid(column=2, row=5, columnspan=2)

# Search Password
search = Button(text="Search", command=find_password)
search.grid(column=3, row=2)

window.mainloop()
