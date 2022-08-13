from array import array
from cProfile import label
from distutils import command
import glob
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from tkinter.tix import COLUMN
root = Tk()

def create_note():
    newwindow = Toplevel(root)
    newwindow.geometry('300x250')
    name_note = Label(newwindow, text='Name')
    name_note.grid(column=0, row=0, pady=10, padx=130)
    entry_name_note = Entry(newwindow, width=40)
    entry_name_note.grid(column=0, row=1)
    tags_note = Label(newwindow, text='Tags(ex: Tools, home, food, revenue)')
    tags_note.place(y=108, x=45)
    entry_tags_note = Entry(newwindow, width=40)
    entry_tags_note.grid(column=0, row=3, pady=80)
    def save_note():
        name = str(entry_name_note.get())
        with open(f'teste0014/Texts/{name}.txt', 'w+', encoding='utf-8') as note:
            note.readline()
        newwindow.destroy()
        window_edit = Toplevel(root)
        window_edit.geometry('800x600')
        scroll = Scrollbar(window_edit)
        scroll.pack(side=RIGHT, fill=Y)
        text_edit = Text(window_edit, yscrollcommand=scroll.set)
        text_edit.pack(fill=BOTH, ipady=90)
        scroll.config(command=text_edit.yview)
        def save_note_edit():
            list_arc = []
            text = text_edit.get('1.0', 'end')
            archives = glob.glob('teste0014/Texts/*')
            for archive in archives:
                arc1 = f'{archive[archive.index("Texts") + 6:]}'
                list_arc.append(arc1)
            with open(f'teste0014/View_text.txt', 'w+') as notes:
                notes.truncate()
            with open(f'teste0014/View_text.txt', 'a+', encoding='utf-8') as notes:
                for item in list_arc:
                    notes.write(f'{item.replace(".txt", "")}\n')
                list_arc.clear()
            with open(f'teste0014/Texts/{name}.txt', 'w+', encoding='utf-8') as note:
                note.write(f'{text}')
            window_edit.destroy()
        button_save = Button(window_edit, text='Save', command=save_note_edit)
        button_save.place(x=750, y=570)
    save_note_button = Button(newwindow, text='Save', command=save_note)
    save_note_button.place(x=250, y=210)
def view_note():
    list_arc= []
    archives = glob.glob('teste0014/Texts/*')
    for archive in archives:
        arc1 = f'{archive[archive.index("Texts") + 6:]}'
        list_arc.append(arc1)
    with open(f'teste0014/View_text.txt', 'w+') as notes:
        notes.truncate()
    with open(f'teste0014/View_text.txt', 'a+', encoding='utf-8') as notes:
        for item in list_arc:
            notes.write(f'{item.replace(".txt", "")}\n')
    with open(f'teste0014/View_text.txt', 'r+', encoding='utf-8') as view_note:
        lines = view_note.readlines()
    label_view_notes['text'] = ''
    label_view_notescolumn1['text'] = ''
    for index, notes in enumerate(lines):
        if index <= 10:
            label_view_notes['text'] += f'{index + 1} - {notes}\n'
        else:
            label_view_notescolumn1['text'] += f'{index + 1} - {notes}\n'
def edit_delete():
    def delete_note():
        try:
            file = list_archi[int(entry_option.get()) - 1]
            os.remove(file)
            window_edit_delete.destroy()
        except:
            print('\033[31mErro, not a number or is 0, or dont exist\033[m\n')
    def edit_note():
        try:
            num = int(entry_option.get()) - 1
            file = list_archi[num]
            window_edit = Toplevel(root)
            window_edit.geometry('800x600')
            scroll = Scrollbar(window_edit)
            scroll.pack(side=RIGHT, fill=Y)
            text_edit = Text(window_edit, yscrollcommand=scroll.set)
            text_edit.pack(fill=BOTH, ipady=90)
            scroll.config(command=text_edit.yview)
            window_edit_delete.destroy()
            def save_edit():
                text = text_edit.get('1.0', 'end')
                with open(file, 'a+', encoding='utf-8') as edit_note:
                    edit_note.write(text)     
                window_edit.destroy()
            button_save = Button(window_edit, text='Save', command=save_edit)
            button_save.place(x=750, y=570)
        except:
            print('\033[31mErro, not a number or is 0, or dont exist\033[m\n')
    def view_content_note():
        try:
            file_path = int(entry_option.get()) - 1
            path = list_archi[file_path]
            def content():
                content = []
                with open(path, 'r+', encoding='utf-8') as view_content_note:
                    lines = view_content_note.readlines()
                    for line in lines:
                        content += line
                label_contcont['text'] = content
            
            
            window_view_content_note = Toplevel(root)
            window_view_content_note.geometry('800x600')
            label_contcont = Label(window_view_content_note, text='')
            print(label_contcont['text'])
            Text_content = Text(window_view_content_note)
            Text_content.grid(column=0, row=0)
            Text_content.insert(INSERT, str('ada'))

            sb = Scrollbar(window_view_content_note, orient=VERTICAL)
            sb.grid(row=0, column=1, sticky=NS)
            Text_content.config(yscrollcommand=sb.set)
            sb.config(command=Text_content.yview)
            content()
        except:
            print('\033[31mErro, not a number or is 0, or dont exist\033[m\n')
    archives = glob.glob('teste0014/Texts/*')
    list_archi = []
    for archive in archives:
        archi = f'{archive.replace(archive[15], "/")}'
        list_archi.append(archi)
    window_edit_delete = Toplevel(root)
    window_edit_delete.geometry('300x260')
    label_option = Label(window_edit_delete, text='Choice the number of archive')
    label_option.grid(column=0, row=0)
    entry_option = Entry(window_edit_delete)
    entry_option.grid(column=0, row=1)
    label_delete = Label(window_edit_delete, text='Delete a archive')
    label_delete.grid(column=0, row=2)
    button_delete = Button(window_edit_delete, text='Delete' ,background='#DC143C', activebackground='#800000', command=delete_note)
    button_delete.grid(column=0, row=3, padx=100, pady=0, ipadx=30, ipady=10)
    label_edit = Label(window_edit_delete, text='Edit a archive')
    label_edit.grid(column=0, row=4)
    button_edit = Button(window_edit_delete, text='Edit' ,background='#32CD32', activebackground='#006400', command=edit_note)
    button_edit.grid(column=0, row=5, padx=100, pady=0, ipadx=30, ipady=10)
    label_view_content_note = Label(window_edit_delete, text='View a archive')
    label_view_content_note.grid(column=0, row=6)
    button_view_content_note = Button(window_edit_delete, text='View' ,background='#32CD32', activebackground='#006400', command=view_content_note)
    button_view_content_note.grid(column=0, row=7, padx=100, pady=0, ipadx=30, ipady=10)
x = 980
y = 650
root.geometry(f'{x}x{y}')
root.config(background='#483D8B')
frame = Frame(root, background='#4682B4', borderwidth=5, relief='ridge')
frame.place(x=730, y=0, width=250, height=650)
photo_button_create = PhotoImage(file='teste0014/add.png')
label_create = Label(frame, text='Create new', background='#4682B4')
label_create.place(x=74, y=42)
label_create.config(font=(13))
button_create = Button(frame, image=photo_button_create, background='blue', activebackground='#00008B', command=create_note)
button_create.place(x=159, y=40)
label_view_notes = Label(root, text='Press Update notes', background='#483D8B')
label_view_notes.place(x=30, y=7)
label_view_notes.config(font=("Courier", 20))
label_update = Label(frame, text='Update notes', background='#4682B4')
label_update.place(x=60, y=102)
label_update.config(font=(13))
photo_button_update = PhotoImage(file='teste0014/update.png')
button_update = Button(frame, image=photo_button_update, background='blue', activebackground='#00008B', command=view_note)
button_update.place(x=159, y=100)
label_view_notescolumn1 = Label(root, text='', background='#483D8B')
label_view_notescolumn1.place(x=370, y=7)
label_view_notescolumn1.config(font=("Courier", 20))
photo_button_created_edit = PhotoImage(file='teste0014/edit.png')
label_edit_notes_created = Label(frame, text='Edit', background='#4682B4')
label_edit_notes_created.place(x=111, y=164)
label_edit_notes_created.config(font=(13))
button_edit_notes_created = Button(frame, text='', image=photo_button_created_edit, background='blue', activebackground='#00008B', command=edit_delete)
button_edit_notes_created.place(x=159, y=164)
root.mainloop()
