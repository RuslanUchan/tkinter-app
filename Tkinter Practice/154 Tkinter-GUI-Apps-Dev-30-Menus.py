import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        menu = tk.Menu(self)
        file_menu = tk.Menu(menu, tearoff=0) # deactivate detaching menus from window

        file_menu.add_command(label="New File")
        file_menu.add_command(label="Open")
        file_menu.add_separator()
        file_menu.add_command(label="Save")
        file_menu.add_command(label="Save as...")

        menu.add_cascade(label="File", menu=file_menu)
        menu.add_command(label="About")
        menu.add_command(label="Quit", command=self.destroy)
        
        # attaching the menu to top-level window
        # each top-level window can only have one menu bar configured
        self.config(menu=menu)

        # Notes
        # add_command usually called with command option
        # which is callback invoked when the entry is clicked
        # there are no arguments passed, like button widgets

if __name__ == "__main__":
    app = App()
    app.mainloop()