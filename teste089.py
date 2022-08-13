from asyncio import threads
import threading
from tkinter import *
import keyboard
from threading import Thread as Td
from time import sleep

x = 0
y = 0
mov_x = 1
mov_y = 1

def Jump():
    c = 0
    velocity = -0.65
    while True:
        c += velocity
        sleep(0.05)
        canvas.move(snake, 0, c)
        if c <= -0.30:
            velocity = 0.65
        if c >= 0.34:
            velocity = 0
            c=0
            break
        
def Kill_Td(td):
    try:
        td.join()
    except:
        print("Thread is dead")

def Key():
    global x, y, mov_x, mov_y, td

    while True:
        
        if keyboard.is_pressed("a"):
            print("Pressed \033[33mA\033[m", 1)
            x -= mov_x
        if keyboard.is_pressed("d"):
            print("Pressed \033[33mD\033[m", 1)
            x += mov_x
        if keyboard.is_pressed("space"):
            td = Td(target=Jump).start()
            Kill_Td(td)
            print(len(threading.enumerate()))
        if canvas.coords(snake)[0] <= 0:
            mov_x = 0
            if keyboard.is_pressed("d"):
                mov_x = 1
        if canvas.coords(snake)[0] >= 765:
            mov_x = 0
            if keyboard.is_pressed("a"):
                mov_x = 1
        canvas.move(snake, x, y)
        x = 0
        y = 0


root = Tk()
root.geometry("800x600")
canvas = Canvas(root, width=800, height=600)
snake = canvas.create_oval(510, 560, 545, 595, width=2, fill="black")
canvas.place(x=0, y=0)
Td(target=Key).start()
root.mainloop()
