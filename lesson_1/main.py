# Programmering i Python
# Seminar 1
#   Author: Zephyro Kemstedt

import tkinter as tk

window = tk.Tk()


def send_text() -> None:
    text_field.insert(tk.END, f'{text_entry.get()}\n')


title = tk.Label(text='This is the program name')
text_entry = tk.Entry(width=50)
send_button = tk.Button(text='send', height=7, width=25, command=send_text)
text_field = tk.Text()

title.pack()
text_entry.pack()
send_button.pack()
text_field.pack()

window.mainloop()
