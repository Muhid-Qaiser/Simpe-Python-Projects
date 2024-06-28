from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
import json

# ---------------------------- WEBSITE SEARCHER ------------------------------- #


def find_password():
    website = website_entry.get()

    # if data file doesn't exist
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message=f"No Data File Found\n")

    else:
        # If website is not entered in the data file
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}\n")
        else:
            messagebox.showinfo(title='Oops', message=f"No Details for the website exists\n")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    """Generates a new strong password for the user"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # Appending letters
    password_list += [choice(letters) for _ in range(randint(8, 10))]

    # Appending symbols
    password_list += [choice(symbols) for _ in range(randint(2, 4))]

    # Appending Numbers
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    new_password = ''.join(password_list)

    password_entry.insert(0, new_password)

    pyperclip.copy(new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if not empty_input(website, email, password):
        # is_ok = messagebox.askokcancel(title='Confirmation', message=f'Detail Entered: \nEmail: {email} '
        #                                                       f'\nPassword: {password} \nIs it ok to Save?')
        # if is_ok:

        # Read from json file and store data
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # update old data and add new one
            data.update(new_data)

            # overwrite new data in json file
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            delete_entries()

    else:
        messagebox.showinfo(title='Oops', message='Please dont leave any fields empty!')


def delete_entries():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def empty_input(website, email, password):
    return len(website) == 0 or len(email) == 0 or len(password) == 0


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title(string='Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

website_button = Button(text='Search', width=14, command=find_password)
website_button.grid(column=2, row=1)

user_info_label = Label(text='Email/Username:')
user_info_label.grid(column=0, row=2)

email_entry = Entry(width=53)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'my_email@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text='Add', width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
