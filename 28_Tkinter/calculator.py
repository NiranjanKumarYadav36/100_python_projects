import tkinter as tk
from tkinter import ttk
from functools import partial

root = tk.Tk()
root.title('Calculator')

entry = tk.Entry(root, font=('Helvetica', 20))
entry.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky='ew')

buttons = [
    ('9', 1, 0), ('8', 1, 1),
    ('7', 2, 0), ('6', 2, 1),
    ('5', 3, 0), ('4', 3, 1),
    ('3', 4, 0), ('2', 4, 1),
    ('1', 5, 0), ('0', 5, 1),
    ('/', 6, 0), ('*', 6, 1),
    ('-', 7, 0), ('+', 7, 1),
    ('=', 8, 0), ('.', 8, 1),
]


def button_click(value):
    entry.insert(tk.END, value)


def calculate():
    value = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(value))


def clear():
    entry.delete(0, tk.END)


for text, row, column in buttons:
    if text == "=":
        button = ttk.Button(text=text, command=calculate)
    else:
        button = ttk.Button(text=text, command=partial(button_click, text))

    button.grid(row=row, column=column, padx=5, pady=5, sticky='ew')

clear_button = ttk.Button(root, text="C", command=clear)
clear_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5, sticky='ew')


root.mainloop()
