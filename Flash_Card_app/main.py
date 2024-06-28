from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data_frame = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    data_frame = pandas.read_csv('data/french_words.csv')

to_learn = data_frame.to_dict(orient='records')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title(string='Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, next_card)

new_image = PhotoImage(file='images/card_back.png')
old_image = PhotoImage(file='images/card_front.png')
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=old_image)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
