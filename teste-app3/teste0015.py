from posixpath import basename
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import pygame
from tkinter import *

def atention():
    window = Tk()
    window.geometry('250x110')
    window.resizable(0, 0)
    label_atention = Label(window, text='Atention, not move musics for others path if you move a music delete and add again', wraplength='250')
    label_atention.grid(column=0, row=0)
    label_atention.config(font=('Courier'))
    button_exit = Button(window, text='Continue', command=window.destroy)
    button_exit.place(x=160, y=80)
    window.mainloop()
atention()
root = Tk()
root.title('Music player')
root.geometry('400x500')
root.config(background='#4F4F4F')
root.resizable(0, 0)
pygame.mixer.init()
music = 'nothing'
music_selected = ''
music_is = ''
list_txt_music = []
frame = Frame(root, background='#87CEEB')
frame.place(x=0, y=270)
frame.config(width=1000, height=110)

def volume_music(volume):
    vol = float(volume)/100
    print(volume)
    pygame.mixer.music.set_volume(vol)

def delete_music():
    file = list_musics.curselection()
    file = list_txt_music[file[0]][0].strip()
    with open('teste0015/list_musics.txt', 'r+', encoding='utf-8') as view:
        view = view.readlines()
    with open('teste0015/list_musics.txt', 'w+', encoding='utf-8') as delete:
        for i, line in enumerate(view):
            if file != line.strip():
                delete.write(line)
            else:
                list_musics.delete(i)

def add_music():
    ask_music = askopenfilename()
    add_music_again = False
    for veri in list_txt_music:
        for veri_in in veri:
            if veri_in.strip() == ask_music.strip():
                add_music_again = True
            else:
                print('this music existe in list')
    if add_music_again == False:
        with open('teste0015/list_musics.txt', 'a+', encoding='utf-8') as list:
            list.write(f'{ask_music.strip()}\n')
        with open('teste0015/list_musics.txt', 'r+', encoding='utf-8') as play_list:
            musics_list = play_list.readlines()
        list_txt_music.clear()
        for index, musics in enumerate(musics_list):
            print(f'\033[32m{musics}\033[m')
            list_txt_music.append([musics]) 
        print(f'\033[35m{list_txt_music}\033[m')
        i = 0
        for index, musics in enumerate(list_txt_music):
            i += index
        list_musics.insert(i, basename(ask_music))
        print(i)
    else:
        messagebox.showwarning(title='Warning', message=f'{basename(ask_music)} music already exist')
def music_play():
    global music
    global music_selected

    file = list_musics.curselection()
    file = list_txt_music[file[0]][0].strip()
    print(f'\033[31m{file}\033[m')
    label_music_playing['text'] = basename(file)
    if music == 'nothing' or file != music_selected:
        music_selected = file.strip()
        pygame.mixer.music.load(f'{file}')
        pygame.mixer.music.play()
        music = 'played'
        print(f'\033[32mThe music is: {music}\033[m')

    elif music == 'paused':
        music = 'played'
        print(f'\033[32mThe music is: {music}\033[m')
        pygame.mixer.music.unpause()

    elif music == 'played':
        music = 'paused'
        print(f'\033[32mThe music is: {music}\033[m')
        pygame.mixer.music.pause()

list_musics = Listbox(root)
list_musics.pack(fill=X, ipady=1)
list_musics.config(background='#808080', relief='flat', highlightthickness=0, bd=0)
list_musics.config(font=('Georgia', 8))
with open('teste0015/list_musics.txt', 'r+', encoding='utf-8') as play_list:
    musics_list = play_list.readlines()
for index, musics in enumerate(musics_list):
    print(f'\033[32m{musics}\033[m')
    list_txt_music.append([musics.strip()])     
    list_musics.insert(index, basename(musics.strip()))
print(f'\033[35m{list_txt_music}')
scroll_list_music = Scrollbar(list_musics)
scroll_list_music.pack(side=RIGHT, ipady=50)
list_musics.config(yscrollcommand=scroll_list_music.set)
scroll_list_music.config(command=list_musics.yview)

image_play = PhotoImage(file='teste0015/icons/play.png')
button_play = Button(root, image=image_play, background='#4F4F4F', activebackground='#363636', highlightthickness=0, bd=0, command=music_play)
button_play.place(x=190, y=400)

image_add = PhotoImage(file='teste0015/icons/add.png')
label_add_music = Label(root, text='Add new music', background='#4F4F4F')
label_add_music.place(x=292, y=160)
label_add_music.config(font=('sans', 8))
button_add_music = Button(root, image=image_add, background='#4F4F4F',activebackground='#363636', highlightthickness=0, bd=0, command=add_music)
button_add_music.place(x=374, y=160)

label_delete_music = Label(root, text='Delete a music', background='#4F4F4F')
label_delete_music.place(x=300, y=194)
label_delete_music.config(font=('sans', 8))
image_del = PhotoImage(file=('teste0015/icons/delete.png'))
button_del_music = Button(root, image=image_del, background='#4F4F4F', activebackground='#363636', highlightthickness=0, bd=0, command=delete_music)
button_del_music.place(x=374, y=194)

label_music_playing = Label(root, text='Nothing music', background='#87CEEB', wraplength=350)
label_music_playing.pack(pady=130)
label_music_playing.config(font=('Georgia', 12))
label_scale = Label(root, text='Volume', background='#4F4F4F')
label_scale.place(x=310, y=428)
label_scale.config(font=('sans', 8))
volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, background='#4F4F4F', activebackground='#363636', highlightthickness=0, bd=0, command=volume_music)
volume_scale.place(x=290, y=450)
volume_scale.set('30')
pygame.mixer.music.set_volume(0.3)
root.mainloop()
