from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.eval("tk::PlaceWindow . center")


def create_button(text, column, row, **kwargs):
    button = Button(text=text, highlightthickness=0, **kwargs)
    button.grid(column=column, row=row)
    return button


def create_label(text, column, row, **kwargs):
    label = Label(text=text, bg=YELLOW, fg=GREEN, **kwargs)
    label.grid(column=column, row=row)
    return label


title = create_label("Timer", column=1, row=0, font=(FONT_NAME, 40, "bold"))
checkmark = create_label(CHECKMARK, column=1, row=3, font=(FONT_NAME, 20, "bold"))
start_button = create_button("Start", column=0, row=2)
reset_button = create_button("Reset", column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
