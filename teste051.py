from tkinter import *
janela = Tk()
janela.title('Calculadora')
janela.geometry('220x60')
text1 = Label(janela, text='Calculadora')
text1.grid(column=0, row=0)
num1 = Entry(janela)
num1.grid(column=1, row=0)

def calculadora():
    rst = 0
    while True:
        n = num1.get()
        if n.count('+') >= 1:
            a = n.split('+')
            if a[0].isnumeric() == True:
                for num in range(0, len(a)):
                    b = float(a[num])
                    rst += b
            else:
                for num in range(0, len(a)):
                    if num > 0:
                        b = float(a[num])
                        rst += b
        elif n.count('-') >= 1:
            a = n.split('-')
            if a[0].isnumeric() == True:
                for num in range(0, len(a)):
                    b = float(a[num])
                    rst -= b
            else:
                for num in range(0, len(a)):
                    if num > 0:
                        b = float(a[num])
                        rst -= b
        elif n.count('x') >= 1:
            a = n.split('x')
            if a[0].isnumeric() == True:
                for num in range(0, len(a)):
                    b = float(a[num])
                    rst *= b
            else:
                for num in range(0, len(a)):
                    if num > 0:
                        b = float(a[num])
                        rst *= b
        elif n.count('/') >= 1:
            a = n.split('/')
            if a[0].isnumeric() == True:
                rst = float(a[0]) / float(a[1])
            else:
                rst = rst / float(a[1])
        r['text'] = rst
        break
botao = Button(janela, text='Resultado', command=calculadora)
botao.grid(column=0, row=1)
r = Label(janela, text='')
r.grid(column=1, row=1)

janela.mainloop()

