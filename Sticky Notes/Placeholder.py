import tkinter as tk

class Placeholder(tk.Frame):
    """A placeholder for notes in the main window. Lists all note's title, contents and edit button"""

    def __init__(self, master, items=[]):
        super().__init__(master)

        self.notes = items

        for i, note in enumerate(self.notes):
            col = i % 4
            row = i // 4

            self.note_title = note[0:-4]

            self.note_frame = tk.LabelFrame(self, padx=15, pady= 15, text=self.note_title)
            self.note_frame.grid(row=row, column=col, padx=10, pady=10, sticky=tk.NW)
            
            with open(note, 'r') as f:
                contents = f.read()

            self.contents_label = tk.Label(self.note_frame, text=contents)
            self.contents_label.pack(side=tk.TOP, expand=1, fill=tk.BOTH)

            self.edit_notes_btn = tk.Button(self.note_frame, text="Edit", relief=tk.GROOVE, command=self.openNote)
            self.edit_notes_btn.pack(side=tk.BOTTOM, fill=tk.BOTH, pady=(10,0))

    def openNote(self, event):
        pass

"""
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        # control = [1, 1]
        note = ["notes.txt", "GGWP.txt"]
        # controlled_items = list(zip(control, items))
        self.the_note = Placeholder(self, note)
        self.the_note.pack()
"""

### CODE MIGRATED TO STICKY NOTES ALREADY ###

if __name__ == "__main__":
    app = App()
    app.mainloop()