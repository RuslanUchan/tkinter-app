# Application to monitor my time left to live

import tkinter as tk
from tkinter import *
import datetime

dead = datetime.datetime(2022, 5, 13, 0, 0, 0)
today = datetime.datetime.today()

till_dead = dead - today
#print("You've got", till_dead.days, "days before you're dead.")

window = tk.Tk()
window.title("Your Time Left")
window.geometry('400x250')

clock_frame = tk.Label(window, font = ('times', 20), bg = 'white', fg = 'black')
clock_frame.pack(fill = 'both', expand = 1)

display_text = "Hello there :)\nYou've got " + str(till_dead.days) + " days left\nbefore your loved ones reach her\nsupposed to be marriage time.\nUse your time wisely."
clock_frame.config(text = display_text)

window.mainloop()