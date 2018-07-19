import tkinter as tk

RELIEFS = [tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE,tk.FLAT]

class ButtonApp(tk.Tk):
    def __init__(self):
        super().__init__()
        #self.img = tk.PhotoImage(file="python.png")
        self.btn = tk.Button(self, text="Button with image", compound=tk.LEFT, command=self.disable_btn) #image = self.img, 
        self.btns = [self.create_btn(r) for r in RELIEFS]
        self.btn.pack()

        for btn in self.btns:
            btn.pack(padx=10, pady=10, side=tk.LEFT)

    def create_btn(self, relief):
        return tk.Button(self, text=relief, relief=relief)

    def disable_btn(self):
        self.btn.config(state=tk.DISABLED)

if __name__=="__main__":
    app = ButtonApp()
    app.mainloop()