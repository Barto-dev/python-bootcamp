from tkinter import *
from tkinter import messagebox
from day_5.password_generator import generate_password

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

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops", message="Please don't leave any fields empty!"
        )
        return

    is_ok = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?",
    )

    if is_ok:
        with open("data.csv", "a") as file:
            file.write(f"{website},{email},{password}\n")
        clear_inputs()


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
website_input = create_entry(width=40, column=1, row=1, columnspan=2)
website_input.focus()

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
