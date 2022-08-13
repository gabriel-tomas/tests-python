from tkinter import *
def create_note():
    note = entry_create.get()
    if bool(note) == True:
        with open('teste0013/notes.txt', 'a+', encoding='utf-8') as adction_note:
            adction_note.write(f'{note}\n')
c = 0
def view_note():
    try:
        with open('teste0013/notes.txt', 'r+', encoding='utf-8') as view_note:
            lines = view_note.readlines()
            label_view['text'] = ''
            for index, line_per_line in enumerate(lines):
                label_view['text'] += f'{index + 1}  - {line_per_line}\n'
    except:
        label_view['text'] = 'Error, Nothing here'
def delete_note():
    with open('teste0013/notes.txt', 'w+', encoding='utf-8') as delete_note:
        delete_note.truncate()
window = Tk()
window.config(background='#00ffff')
window.title('Notes')
window.geometry('250x300')
window.iconbitmap('teste0013/icon.ico')
aba_main = Frame(window, background='#808080', borderwidth=2, relief='sunken')
aba_main.place(x=5, y=35, width=150, height=260)
entry_create = Entry(window, width=27)
entry_create.grid(column=0, row=0)
button_create = Button(window, text='Create note', command=create_note)
button_create.grid(column=1, row=0, rowspan=1, padx=5)
button_update = Button(window, text='Update notes', command=view_note)
button_update.grid(column=1, row=1, padx=2, pady=5)
button_delete_notes = Button(window, text='Delete notes', command=delete_note)
button_delete_notes.grid(column=1, row=2, padx=2, pady=5)
label_view = Label(aba_main, text='', background='#808080', wraplength=140)
label_view.grid(column=0, row=1, padx=2)
window.mainloop()
