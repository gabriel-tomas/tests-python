from tkinter import *

class App:
    def __init__(self, master):
        self.c = 0
        self.root = master
        self.root.geometry("400x200")
        self.root.title("App")
        self.root.resizable(0, 0)
        self.label = Label(self.root, text="Clicks:")
        self.label.place(x=170, y=70)
        self.label.config(font=(23))
        self.button = Button(self.root, text="Iniciar contador", command=self.count)
        self.button.place(x=155, y=100)
    def count(self):
        self.c += 1
        self.label["text"] = f"Clicks: {self.c}"

c = 0
def count():
    global c

    c += 1
    label["text"] = f"Clicks: {c}"
root = Tk()
root.geometry("400x200")
root.title("App")
root.resizable(0, 0)
label = Label(root, text="Clicks:")
label.place(x=170, y=70)
label.config(font=(23))
button = Button(root, text="Iniciar contador", command=count)
button.place(x=155, y=100)
root.mainloop()

