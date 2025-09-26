from tkinter import *
from PIL import ImageTk, Image

BACKGROUND_COLOR = "#B1DDC6"
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flash The Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
#
canvas = Canvas(height=800, width=526)
card
canvas.grid(row=0, column=0, columnspan=2)

# #Labels
# title_label = Label(text="Title", height=40, width=40)
# title_label.grid(row=0, column=1)
# word_label = Label(text="Word")
# word_label.grid(row=0, column=1)
#
# #
# # #Entries
# # website_entry = Entry(width=21)
# # website_entry.grid(row=1, column=1)
# # website_entry.focus()
# # email_entry = Entry(width=35)
# # email_entry.grid(row=2, column=1, columnspan=2)
# # email_entry.insert(0, "angela@gmail.com")
# # password_entry = Entry(width=21)
# # password_entry.grid(row=3, column=1)
#
#
# Buttons

right_button_image = PhotoImage(file="right_button.png")
right_button = Button(height= 240, width=240, image=right_button_image, highlightthickness=0)
# right_button = Button(command=find_password)
right_button.grid(row=1, column=0)


wrong_button_image = PhotoImage(file="wrong_button.png")
wrong_button = Button(height= 240, width=240, image=wrong_button_image, highlightthickness=0)
# wrong_button = Button(command=find_password)
wrong_button.grid(row=1, column=1)
#
window.mainloop()