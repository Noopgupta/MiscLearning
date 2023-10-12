import random
import pandas
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

german_words = pandas.read_csv("data/german_words.csv")
data_dict = german_words.to_dict(orient="records")
current_word = {}


def start_game():
    global current_word
    current_word = random.choice(data_dict)
    canvas.itemconfig(title_text, text="German")
    canvas.itemconfig(word_text, text=current_word["German"])
    window.after(2000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=current_word["English"])


window = Tk()
window.title("Flash The Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)



canvas = Canvas(height=400, width=400)
card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(200, 100, image=card_front_image)
title_text = canvas.create_text(200, 100, text="Press tick button", font=("Ariel", 20, "italic"))
word_text = canvas.create_text(200, 200, text="to continue", font=("Ariel", 20, "italic"))
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button_image = PhotoImage(file="images/right.png")
right_button = Button(height=100, width=100, image=right_button_image, highlightthickness=0, command=start_game)
right_button.grid(row=1, column=0)
#
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(height=100, width=100, image=wrong_button_image, highlightthickness=0, command=flip_card)
wrong_button.grid(row=1, column=1)

window.mainloop()
