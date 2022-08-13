from tkinter import *
def um(text):
    ent1.insert(END, text)
def dois(text):
    ent1.insert(END, text)
def tres(text):
    ent1.insert(END, text)
def quatro(text):
    ent1.insert(END, text)
def cinco(text):
    ent1.insert(END, text)
def seis(text):
    ent1.insert(END, text)
def sete(text):
    ent1.insert(END, text)
def oito(text):
    ent1.insert(END, text)
def nove(text):
    ent1.insert(END, text)
def soma(text):
    ent1.insert(END, text)
def zero(text):
    ent1.insert(END, text)
def multiplicacao(text):
    ent1.insert(END, text)
def divisao(text):
    ent1.insert(END, text)
def apagar():
    ent1.delete(0, END)
def calcular():
    resultado = 0
    resultmulti = 1
    r_entry = ent1.get()
    if r_entry.count('+') >= 1:
        splt_nums = r_entry.split('+')
        for n in splt_nums:
            resultado += float(n)
    if r_entry.count('x') >= 1:
        splt_nums = r_entry.split('x')
        for n in splt_nums:
            resultmulti *= float(n)
            resultado = resultmulti
    if r_entry.count('/') >= 1:
        splt_nums = r_entry.split('/')
        resultado = float(splt_nums[0]) / float(splt_nums[1])
        
    ent1.delete(first=0, last=len(r_entry))
    ent1.insert(END, resultado)
main = Tk()

ent1 = Entry(main, justify=CENTER)
ent1.grid(column=0, row=0, columnspan=3, ipadx=10, ipady=10)

bt1 = Button(main, text='1', command= lambda:um('1'))
bt1.grid(column=0, row=1, ipadx=10, ipady=10)

bt2 = Button(main, text='2', command= lambda:dois('2'))
bt2.grid(column=1, row=1, ipadx=10, ipady=10)

bt3 = Button(main, text='3', command= lambda:tres('3'))
bt3.grid(column=2, row=1, ipadx=10, ipady=10)

bt4 = Button(main, text='4', command= lambda:quatro('4'))
bt4.grid(column=0, row=2, ipadx=10, ipady=10)

bt5 = Button(main, text='5', command= lambda:cinco('5'))
bt5.grid(column=1, row=2, ipadx=10, ipady=10)

bt6 = Button(main, text='6', command= lambda:seis('6'))
bt6.grid(column=2, row=2, ipadx=10, ipady=10)

bt7 = Button(main, text='7', command= lambda:sete('7'))
bt7.grid(column=0, row=3, ipadx=10, ipady=10)

bt8 = Button(main, text='8', command= lambda:oito('8'))
bt8.grid(column=1, row=3, ipadx=10, ipady=10)

bt9 = Button(main, text='9', command= lambda:nove('9'))
bt9.grid(column=2, row=3, ipadx=10, ipady=10)

bt10 = Button(main, text='=', command=calcular)
bt10.grid(column=3, row=1, ipadx=5, ipady=5)

bt11 = Button(main, text='+', command= lambda:soma('+'))
bt11.grid(column=3, row=2, ipadx=5, ipady=5)

bt12 = Button(main, text='0', command= lambda:zero('0'), justify=CENTER)
bt12.grid(column=1, ipadx=10, ipady=10)

bt13 = Button(main, text='x', command= lambda:multiplicacao('x'))
bt13.grid(column=3, row=3, ipadx=5, ipady=5)

bt14 = Button(main, text='/', command= lambda:divisao('/'))
bt14.grid(column=3, row=4, ipadx=5, ipady=5)

bt15 = Button(main, text='C', command=apagar)
bt15.grid(column=3, row=0, ipadx=5, ipady=5)

main.mainloop()
