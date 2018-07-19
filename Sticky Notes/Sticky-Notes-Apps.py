import tkinter as tk
import os

PATH = "/Users/Rusla/OneDrive/Documents/100-Projects/Python/Tkinter/Sticky Notes"

class Notes(tk.Toplevel):
    """Notes that pop up after function add_notes called from App class"""

    def __init__(self, parent):
        super().__init__(parent)

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


class Placeholder(tk.Frame):
    """A placeholder for notes in the main window. Lists all note's title, contents and edit button"""

    def __init__(self, parent, items=[]):
        super().__init__(parent)

        self.notes = items # pass function values to local var
        self.records = [] # variable to keep track of title and notes

        for i, note in enumerate(self.notes):
            col = i % 4
            row = i // 4

            self.note_title = note[0:-4]

            self.note_frame = tk.LabelFrame(self, padx=15, pady= 15, text="{}-{}".format(i, self.note_title))
            self.note_frame.grid(row=row, column=col, padx=10, pady=10, sticky=tk.NW)
            
            with open(note, 'r') as f:
                self.contents = f.read()

            # Keep it both in records
            self.records.append(list(zip(self.note_title, self.contents)))

            # Widgets
            self.contents_label = tk.Label(self.note_frame, text=self.contents)
            self.contents_label.pack(side=tk.TOP, expand=1, fill=tk.BOTH)
        

class Main(tk.Tk):
    """Sticky notes Main application"""

    def __init__(self, countAndSales):
        super().__init__()
        
        # Tk's elements
        self.title("Sticky Notes Apps")
        self.geometry("800x600")
        self.resizable(0, 0)

        # Class Attributes
        self.file_list, self.notes_count = countAndSales # Function passed to Main
        self.notes_instance = []
        self.index = tk.IntVar()

        # Passing arguments to Placeholder instance 
        self.the_note = Placeholder(self, self.file_list) 
        
        # Widgets
        self.edit_group = tk.LabelFrame(self, text="Edit")

        self.add_notes_btn = tk.Button(self, text="Add Note", command=self.addNotes) # Add notes
        self.notes_count_label = tk.Label(self, text="Notes count: {}".format(self.notes_count)) 

        self.edit_notes_label = tk.Label(self.edit_group, text="Enter Notes Number")
        self.edit_notes_entry = tk.Entry(self.edit_group, textvariable=self.index)

        # Get entry values
        # self.index = self.edit_notes_entry.get()
        self.edit_notes_btn = tk.Button(self.edit_group, text="Confirm", command=self.editNotes)
        
        
        # Pack Widgets
        self.add_notes_btn.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        self.edit_group.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)
        self.notes_count_label.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

        self.edit_notes_label.pack(side=tk.LEFT, padx=10, pady=10, expand=1, fill=tk.X, anchor='n')
        self.edit_notes_entry.pack(side=tk.LEFT, padx=10, pady=10, expand=1, fill=tk.X, anchor='n')
        self.edit_notes_btn.pack(side=tk.LEFT, padx=10, pady=10, expand=1, fill=tk.X, anchor='n')

        self.the_note.pack(padx=10, pady=10, anchor='center') # All notes pack

    # Methods
    def addNotes(self):
        window = Notes(self)
        window.grab_set()

    def editNotes(self):
        window = Notes(self)
        sel_title, sel_notes = self.the_note.records[self.index.get()]

        window.title_entry.insert(0, sel_title)
        window.notes_text.insert("1.0", sel_notes)

        window.grab_set()


def _noteCountAndList():
    """Function to count notes and get files from dir"""
    counter = 0
    files = []

    for filename in os.listdir(PATH):
        if filename.endswith('.txt'):
            files.append(filename)
            counter += 1
    
    return (files, counter)
        

if __name__=="__main__":
    app = Main(_noteCountAndList())
    app.mainloop()