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

reps = 0

# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1
    if reps % 8 == 0:
        long_break_sec = LONG_BREAK_MIN * 60
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        short_break_sec = SHORT_BREAK_MIN * 60
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        work_sec = WORK_MIN * 60
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def update_checkmarks():
    marks = ""
    for _ in range(reps // 2):
        marks += CHECKMARK
    checkmark.config(text=marks)


def format_time(time):
    minutes = time // 60
    seconds = time % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{minutes}:{seconds}"


def count_down(count):
    count_text = format_time(count)
    canvas.itemconfig(timer_text, text=count_text)
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_time()
        update_checkmarks()


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
checkmark = create_label(text="", column=1, row=3, font=(FONT_NAME, 20, "bold"))
start_button = create_button("Start", column=0, row=2, command=start_time)
reset_button = create_button("Reset", column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

window.mainloop()
