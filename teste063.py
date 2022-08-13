def infousers():
    from time import sleep
    nome = entradanome.get()
    idade = entradaidade.get()
    with open('Usuários.html', 'a+') as users:
        users.write(f'<li>{nome}</li>\n')
        users.write(f'<p>{idade}</p>\n')
    sleep(2)
    quit()
#Janela
from tkinter import *
janela = Tk()
janela.geometry('250x80')
janela.title('Cadastro')

infonome = Label(janela, text='Nome:')
infonome.grid(column=0, row=0)
entradanome = Entry(janela)
entradanome.grid(column=1, row=0)

infoidade = Label(janela, text='Idade:')
infoidade.grid(column=0, row=1)
entradaidade = Entry(janela)
entradaidade.grid(column=1, row=1)

buttenviar = Button(janela, text='Enviar >', command=infousers)
buttenviar.grid(column=1, row=2)

janela.mainloop()
