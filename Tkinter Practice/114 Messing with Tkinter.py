# Import & Path
import tkinter as tk
# from PIL import ImageTk, Image

# path = "C:/Users/Ruslan Uchan/Documents/100 Projects/Python Code/Python/16329.jpg"

# Setup Window
window = tk.Tk()
window.title("Testing Tkinter")
window.geometry("400x400")
window.configure(background="black")

# Create Label
# img = ImageTk.PhotoImage(Image.open(path))
tk.Label(window, text="Hello World", bg="black", fg="white", font="Times New Roman 12").grid(column=0, row=0, sticky="nw")

window.mainloop()