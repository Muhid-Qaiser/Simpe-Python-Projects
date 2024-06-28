from tkinter import *


def converter():
    miles = int(user_input.get())
    kilo = round(miles * 1.609344)
    kilometer['text'] = kilo


window = Tk()
window.title(string="Miles to Kilometer Converter")
window.minsize(width=220, height=150)
window.config(padx=20, pady=20)

user_input = Entry(width=7)
user_input.grid(column=1, row=0)
user_input.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer = Label()
kilometer.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text='Calculate', command=converter)
calculate_button.grid(column=1, row=2)

mainloop()
