from tkinter import *
from tkinter import messagebox
from day_5.password_generator import generate_password
import json

BG = "white"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password_and_insert():
    password = generate_password(10, 2, 2)
    password_input.delete(0, END)
    password_input.insert(END, password)
    # copy to clipboard
    # piperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def clear_inputs():
    website_input.delete(0, END)
    password_input.delete(0, END)


def save_password():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {"email": email, "password": password}}

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!"
        )
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
            clear_inputs()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
        return None
    except json.decoder.JSONDecodeError:
        messagebox.showerror(title="Error", message="Invalid Data File")
        return None


def find_password(data, website):
    return data.get(website)


def display_password(website, password_data):
    if password_data:
        message = (
            f"Email: {password_data['email']}\nPassword: {password_data['password']}"
        )
        messagebox.showinfo(title=website, message=message)
    else:
        messagebox.showerror(title="Error", message="No Data Found")


def search_password():
    entered_website = website_input.get()
    data = load_data()
    if data:
        password_data = find_password(data, entered_website)
        display_password(entered_website, password_data)


# ---------------------------- UI SETUP ------------------------------- #


def create_label(text, column, row, **kwargs):
    label = Label(text=text, **kwargs)
    label.grid(column=column, row=row)
    return label


def create_entry(width, column, row, columnspan=1, **kwargs):
    entry = Entry(width=width, **kwargs)
    entry.grid(column=column, row=row, columnspan=columnspan)
    return entry


def create_button(text, width, column, row, columnspan=1, **kwargs):
    button = Button(text=text, width=width, **kwargs)
    button.grid(column=column, row=row, columnspan=columnspan)
    return button


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, pady=(0, 20))

website_label = create_label(text="Website: ", column=0, row=1)
website_input = create_entry(width=22, column=1, row=1)
website_input.focus()

search_button = create_button(
    text="Search", width=14, column=2, row=1, command=search_password
)

email_label = create_label(text="Email/Username: ", column=0, row=2)
email_input = create_entry(40, column=1, row=2, columnspan=2)
# insert text in the end of the entry
email_input.insert(END, "example@mail.com")

password_label = create_label(text="Password: ", column=0, row=3)
password_input = create_entry(22, column=1, row=3)
generate_button = create_button(
    text="Generate Password",
    width=14,
    column=2,
    row=3,
    command=generate_password_and_insert,
)

add_button = create_button(
    text="Add", width=37, column=1, row=4, columnspan=2, command=save_password
)


window.mainloop()
