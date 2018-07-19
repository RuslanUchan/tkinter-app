# Trying tkinter library

import random
import tkinter as tk

window = tk.Tk()

window.title("Death Monitoring")
window.geometry("400x400")

def phrase_generator():

    phrases = ["Hello ", "Hi, there ", "Salam "]

    name = str(entry_field1.get())

    return phrases[random.randint(0, 2)] + name

def phrase_display():

    greeting = phrase_generator()

    # below is a text field
    greeting_display = tk.Text(master=window, height=10, width=30)
    greeting_display.grid(column=0, row=3)

    greeting_display.insert(tk.END, greeting)

# Title Label
title = tk.Label(text="Hello, World. This is me trying tkinter", font=("Times New Roman", 20))
title.grid() 

# A Field Entry
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=1)

# Button 
button1 = tk.Button(text="Click me!", bg="red", command=phrase_display)
button1.grid(column=0, row=2)

window.mainloop()