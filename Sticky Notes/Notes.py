import tkinter as tk

class Notes(tk.Tk):
    """Notes that pop up after function add_notes called from App class"""

    def __init__(self):
        super().__init__()

        # Class Attributes
        self.notes_title = tk.StringVar()
        self.notes = tk.StringVar()

        # Widgets
        self.title_label = tk.Label(self, text="Title:")
        self.title_entry = tk.Entry(self)
        self.notes_label = tk.Label(self, text="Notes:")
        self.notes_text = tk.Text(self, width=50, height=20, font="helvetica 8")
        self.save_notes_btn = tk.Button(self, text="Save Notes", command=self.saveNote)
        self.notes_saved_label = tk.Label(self, text="Notes Saved!")

        # Pack Widgets
        self.title_entry.focus_set()
        self.title_label.grid(row=0, column=0, padx=5, sticky='w')
        self.title_entry.grid(row=0, column=1, padx=5, sticky='we')
        self.notes_label.grid(row=1, column=0, padx=5, sticky='w')
        self.notes_text.grid(row=1, column=1, padx=5, sticky='we')
        self.save_notes_btn.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        self.columnconfigure(1, weight=3)

    # Methods
    def confirmNote(self):
        self.notes_title = str(self.title_entry.get()) + ".txt"
        self.notes = self.notes_text.get("1.0", "end-1c")

        # print("{}, {}\n".format(self.notes_title, self.notes))

    def saveNote(self):
        self.confirmNote()

        with open(self.notes_title, 'w') as f:
            f.write(self.notes)

        self.notes_saved_label.grid(row=2, column=1, padx=5,pady=5, sticky='e')        


if __name__=="__main__":
    app = Notes()
    app.mainloop()