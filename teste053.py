from tkinter import *
janela = Tk()
janela.title('Calculadora')

texto1 = Label(janela, text='Calculadora')
texto1.grid(column=0, row=0, padx=60, pady=10)

entrada1 = Entry(janela)
entrada1.grid(column=0, row=1)

def n():
    num = entrada1.get()
    rst = 0
    t1 = ''
    if num.count('+') >= 1:
        n = num.split('+')
        for numeros in n:
            rst += float(numeros)
    if num.count('-') >= 1:
        n = num.split('-')
        for numeros in n:
            rst -= float(numeros)
    if num.count('x') >= 1:
        n = num.split('x')
        for numeros in n:
            rst *= float(numeros)
    if num.count('/') == 1:
        n = num.split('/')
        rst = float(n[0]) / float(n[1])
    if bool(rst) == True:
        rs['text'] = f'Resultado= {rst}'
    else:
        rs['text'] = 'Erro, só é suportado 2 números\n' \
                     'para a divisão'
botao1 = Button(janela, text='Iniciar', command=n)
botao1.grid(column=0, row=2, pady=11)

rs = Label(janela, text='Ainda não existe calculo')
rs.grid(column=0, row=3)


rs1 = Label(janela,text='só é suportado um operador')
rs1.grid(column=0, row=4, pady=13)

botao2 = Button(janela, text='Sair', command=quit)
botao2.grid(column=0, row=5, pady=10)

janela.geometry('200x230', )
janela.mainloop()
