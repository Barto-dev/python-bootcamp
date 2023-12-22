import logging
from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"


class FlashCardApp:
    def __init__(self):
        self.known_button = None
        self.check_img = None
        self.unknown_button = None
        self.cross_img = None
        self.card_word = None
        self.card_title = None
        self.card_background = None
        self.card_back_img = None
        self.card_front_img = None
        self.canvas = None
        self.window = None
        self.current_card = {}
        self.to_learn = self.load_data()
        self.flip_timer = None

    def load_data(self, file_name="data/words_to_learn.csv"):
        try:
            return pandas.read_csv(file_name).to_dict(orient="records")
        except FileNotFoundError:
            logging.exception("File not found, loading default data")
            return pandas.read_csv("data/french_words.csv").to_dict(orient="records")

    def save_data(self, file_name="data/words_to_learn.csv"):
        pandas.DataFrame(self.to_learn).to_csv(file_name, index=False)

    def next_card(self):
        self.window.after_cancel(self.flip_timer)
        self.current_card = choice(self.to_learn)
        self.canvas.itemconfig(self.card_title, text="French", fill="black")
        self.canvas.itemconfig(
            self.card_word, text=self.current_card["French"], fill="black"
        )
        self.canvas.itemconfig(self.card_background, image=self.card_front_img)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def is_known(self):
        self.to_learn.remove(self.current_card)
        self.save_data()
        self.next_card()

    def flip_card(self):
        self.canvas.itemconfig(self.card_title, text="English", fill="white")
        self.canvas.itemconfig(
            self.card_word, text=self.current_card["English"], fill="white"
        )
        self.canvas.itemconfig(self.card_background, image=self.card_back_img)

    def run(self):
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
        self.flip_timer = self.window.after(3000, func=self.flip_card)
        self.canvas = Canvas(width=800, height=526)
        self.card_front_img = PhotoImage(file="images/card_front.png")
        self.card_back_img = PhotoImage(file="images/card_back.png")
        self.card_background = self.canvas.create_image(
            400, 263, image=self.card_front_img
        )
        self.card_title = self.canvas.create_text(
            400, 150, text="Title", font=(FONT, 40, "italic")
        )
        self.card_word = self.canvas.create_text(
            400, 263, text="word", font=(FONT, 60, "bold")
        )
        self.canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.cross_img = PhotoImage(file="images/wrong.png")
        self.unknown_button = Button(
            image=self.cross_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.next_card,
        )
        self.unknown_button.grid(row=1, column=0)
        self.check_img = PhotoImage(file="images/right.png")
        self.known_button = Button(
            image=self.check_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.is_known,
        )
        self.known_button.grid(row=1, column=1)
        self.next_card()
        self.window.mainloop()


if __name__ == "__main__":
    app = FlashCardApp()
    app.run()
