from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = { 
        website: {
            "username": username,
            "password": password,
        }
    }
    
    if website =="" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!") 
    else:
        try:
            with open ("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            #open the new file
            with open ("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating with new data
            data.update(new_data)

            with open ("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            load_file = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in load_file:
            messagebox.showinfo(title=website, message=f"username: {load_file[website]['username']}\npassword: {load_file[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
search_button = Button(text="Search", command=find_password )
search_button.grid(row=1, column=2, columnspan=1)
username_entry = Entry(width=35)
username_entry.insert(0, "Kjagan304@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=password)
generate_password_button.grid(row=3, column=2)
add_button = Button(width=35, text="Add", command= save_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()