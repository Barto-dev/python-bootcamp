from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)


def next_card():
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=(FONT, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(
    image=cross_img, highlightthickness=0, borderwidth=0, command=next_card
)
unknown_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_button = Button(
    image=check_img, highlightthickness=0, borderwidth=0, command=next_card
)
known_button.grid(row=1, column=1)

next_card()
window.mainloop()
