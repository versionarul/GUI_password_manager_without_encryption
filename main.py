import tkinter as tk
from tkinter import messagebox
import password_generator
import pyperclip
import json

LABEL_COLUMN = 0
ENTRY_COLUMN = 1
BUTTON_COLUMN = 2


# -----------------------Pasword Generator ---------------------------------------#


def clicked_button_generate_password():
    entry_password.delete(0, tk.END)
    password = password_generator.generate_password()
    entry_password.insert(0, password)
    pyperclip.copy(password)

# -----------------------Save Password -------------------------------------------#


def clicked_button_add():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()
    new_data = {website:
                    {"email/username":email_username,
                     "password":password,},
    }

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please don't leave any of the fields empty!")
    else:
        is_ok = messagebox.askokcancel(title = website, message=f" These are the entered details : \n Website: {website}  \n Email/Username: {email_username} \n Password: {password}")

        if is_ok:

            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent = 4)

            else:
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent = 4)

            finally:
                entry_website.delete(0, tk.END)
                entry_email_username.delete(0, tk.END)
                entry_password.delete(0, tk.END)


#-------------------------Search by website---------------------------------------#


def clicked_button_search_by_website():
    website = entry_website.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if website in data:
            email_username = data[website]["email/username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Your data for {website}: \nEmail/username: {email_username} \nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message= f"No details for the website: {website} exists!")


#-------------------------Search by email/usename---------------------------------#


def clicked_button_search_by_email_username():
    email_username = entry_email_username.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")
    else:
        if email_username in data:
            websites = []
            for key in data.keys():
                if email_username == data[key]["email/username"]:
                    websites.append(key)
            messagebox.showinfo(title=f"Entries for  {email_username}", message=f"The entries for the {email_username} email/username are: \n{websites}")

        else:
            messagebox.showinfo(title="Error", message= f"No details for the email/username: {email_username} exists!")


#--------------------------Clear all fields---------------------------------------#


def clicked_button_clear_all():
    entry_website.delete(0, tk.END)
    entry_email_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)


# -----------------------UI Setup ------------------------------------------------#


window = tk.Tk()
window.title("Password Manager without encryption")
window.config(padx = 50, pady = 50)

canvas = tk.Canvas(height = 200, width = 200)
logo_img = tk.PhotoImage(file = "logo.png")
canvas.create_image(115, 100 ,image = logo_img) # x, y coordinates for the image
canvas.grid(row = 0, column = ENTRY_COLUMN, pady = 10)

label_website = tk.Label(text = "Website:", width = 20)
label_email_username = tk.Label(text = "Email/Username:", width = 20)
label_password = tk.Label(text = "Password:", width = 20)

label_website.grid(row = 1, column = LABEL_COLUMN)
label_email_username.grid(row = 2, column = LABEL_COLUMN)
label_password.grid(row = 3, column = LABEL_COLUMN)


entry_website = tk.Entry(width = 20)
entry_email_username = tk.Entry(width = 20)
entry_password = tk.Entry(width = 20)

entry_website.grid(row = 1, column = ENTRY_COLUMN)
entry_website.focus()
entry_email_username.grid(row = 2, column = ENTRY_COLUMN)
entry_password.grid(row = 3, column = ENTRY_COLUMN)


button_search_by_website = tk.Button(text = "Search by Website", command = clicked_button_search_by_website, width = 20)
button_search_by_email_username = tk.Button(text = "Search by Email/Username", command = clicked_button_search_by_email_username, width = 20)
button_generate_password = tk.Button(text = "Generate Password", command = clicked_button_generate_password, width = 20)
button_add = tk.Button(text = "Add", command = clicked_button_add, width = 18)
button_clear_all = tk.Button(text = "Clear ALL", command = clicked_button_clear_all, width = 20 )


button_search_by_website.grid(row = 1, column = BUTTON_COLUMN)
button_search_by_email_username.grid(row = 2, column = BUTTON_COLUMN)
button_generate_password.grid(row = 3, column = BUTTON_COLUMN)
button_add.grid(row = 4, column = ENTRY_COLUMN, pady = 10)
button_clear_all.grid(row = 4, column = BUTTON_COLUMN)



tk.mainloop()

