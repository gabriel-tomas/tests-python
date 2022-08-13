from tkinter import ttk
import requests
from tkinter import *
from time import sleep
from bs4 import BeautifulSoup
def cotacoes():
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    req_dic = req.json()
    cot_dolar = req_dic['USDBRL']['bid']
    cot_euro = req_dic['EURBRL']['bid']
    cot_btc = req_dic['BTCBRL']['bid']
    lb1_dolar['text'] = f'Dolar: {cot_dolar}'
    lb2_euro['text'] = f'Euro: {cot_euro}'
    lb3_btc['text'] = f'Bitcoin: {cot_btc}'
def calcular():
    req = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    req_dic = req.json()
    req_ent1 = ent1.get()
    print(req_ent1.isnumeric())
    if bool(req_ent1) == False or bool(req_ent1.isnumeric()) != True:
        lb4_dolar['text'] = f'Dolar: R$0'
        lb5_euro['text'] = f'Euro: R$0'
        lb6_btc['text'] = f'Bitcoin: R$0'
        lb7_info['text'] = 'Erro...'
    elif bool(req_ent1.isnumeric()) == True:
        cot_dolar = req_dic['USDBRL']['bid']
        cot_euro = req_dic['EURBRL']['bid']
        cot_btc = req_dic['BTCBRL']['bid']
        lb4_dolar['text'] = f'Dolar: R$ {float(cot_dolar) * float(req_ent1):.2f}'
        lb5_euro['text'] = f'Euro: R$ {float(cot_euro) * float(req_ent1):.2f}'
        lb6_btc['text'] =f'Bitcoin: R$ {float(cot_btc) * float(req_ent1)}'
        lb7_info['text'] = ''
def noticias():
    req = requests.get('https://g1.globo.com/economia/dolar/')
    bs = BeautifulSoup(req.content, 'html.parser')
    noti_title = bs.find('a', {'class': 'feed-post-link gui-color-primary gui-color-hover'}).text
    noti_resumo = bs.find('div', {'class': 'feed-post-body-resumo'}).text
    lb9['text'] = noti_title.strip()
    lb10['text'] = noti_resumo.strip()
    
janela = Tk()
janela.geometry('300x380')

janela.title('Cotações')
aba1 = ttk.Notebook(janela)
aba1.place(x=0, y=0, width=300, height=380)

aba11 = Frame(aba1, background='#2E8B57')
aba22 = Frame(aba1, background='#3CB371')
aba33 = Frame(aba1, background='#4682B4')
aba1.add(aba11, text='Cotação')
aba1.add(aba22, text='Conversor')
aba1.add(aba33, text='Noticias') 

#Primeira aba, Aba de cotação
bt1 = Button(aba11, text='Atualizar', command=cotacoes)
bt1.grid(column=0, row=0, pady= 23, padx=40, ipadx=40, ipady=7)
bt1.configure(font=('TeX Gyre Adventor', 20))

lb1_dolar = Label(aba11, text='Dolar: ', background='#2E8B57')
lb1_dolar.grid(column=0, row=1, ipady=18, ipadx=54)
lb1_dolar.configure(font=("Avantgarde", 16))

lb2_euro = Label(aba11, text='Euro: ', background='#2E8B57')
lb2_euro.grid(column=0, row=2, ipady=18, ipadx=54)
lb2_euro.configure(font=("Avantgarde", 16))

lb3_btc = Label(aba11, text='Bitcoin: ', background='#2E8B57')
lb3_btc.grid(column=0, row=3, ipady=18, ipadx=54)
lb3_btc.configure(font=("Avantgarde", 16))

bt2 = Button(aba11, text='quit', command=janela.destroy)
bt2.grid(column=0, row=4, pady=23, ipadx=25)
bt2.configure(font=('TeX Gyre Adventor', 15))
#Final da primeira aba, Aba de cotação

#Segunda aba, Aba de conversão
ent1 = Entry(aba22)
ent1.grid(column=1, columnspan=6, row=0, ipadx=20, ipady=3, pady=4)
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
def zero(text):
    ent1.insert(END, text)
def apagar():
    ent1.delete(0, END)

bt1 = Button(aba22, text='1', command= lambda:um('1'), justify=CENTER)
bt1.grid(column=2, row=3, pady=2, ipadx=3, ipady=3)
bt1.configure(font=('Optima'))

bt2 = Button(aba22, text='2', command= lambda:dois('2'), justify=CENTER)
bt2.grid(column=3, row=3, pady=2, ipadx=3, ipady=3)
bt2.configure(font=('Optima'))

bt3 = Button(aba22, text='3', command= lambda:tres('3'), justify=CENTER)
bt3.grid(column=4, row=3, pady=2, ipadx=3, ipady=3)
bt3.configure(font=('Optima'))

bt4 = Button(aba22, text='4', command= lambda:quatro('4'), justify=CENTER)
bt4.grid(column=2, row=2, pady=2, ipadx=3, ipady=3)
bt4.configure(font=('Optima'))

bt5 = Button(aba22, text='5', command= lambda:cinco('5'), justify=CENTER)
bt5.grid(column=3, row=2, pady=2, ipadx=3, ipady=3)
bt5.configure(font=('Optima'))

bt6 = Button(aba22, text='6', command= lambda:seis('6'), justify=CENTER)
bt6.grid(column=4, row=2, pady=2, ipadx=3, ipady=3)
bt6.configure(font=('Optima'))

bt7 = Button(aba22, text='7', command= lambda:sete('7'), justify=CENTER)
bt7.grid(column=2, row=1, pady=2, ipadx=3, ipady=3)
bt7.configure(font=('Optima'))

bt8 = Button(aba22, text='8', command= lambda:oito('8'), justify=CENTER)
bt8.grid(column=3, row=1, pady=2, ipadx=3, ipady=3)
bt8.configure(font=('Optima'))

bt9 = Button(aba22, text='9', command= lambda:nove('9'), justify=CENTER)
bt9.grid(column=4, row=1, pady=2, ipadx=3, ipady=3)
bt9.configure(font=('Optima'))

lb_gambiarra = Label(aba22, background='#3CB371')
lb_gambiarra.grid(column=0, row=5, padx=18)

bt12 = Button(aba22, text='0', command= lambda:zero('0'), justify=CENTER)
bt12.grid(column=3, row=4, pady=2, ipadx=3, ipady=3)
bt12.configure(font=('Optima'))

bt13 = Button(aba22, text='=', command=calcular)
bt13.grid(column=6, row=1)
bt13.configure(font=('Optima'))

bt15 = Button(aba22, text='C', command=apagar)
bt15.grid(column=6, row=2)
bt15.configure(font=('Optima'))

lb4_dolar = Label(aba22, text='Dolar: ', background='#3CB371')
lb4_dolar.grid(column=2, row=5, columnspan=6, pady=7)
lb4_dolar.configure(font=('Mono'))

lb5_euro = Label(aba22, text='Euro:' , background='#3CB371')
lb5_euro.grid(column=2, row=6, columnspan=6, pady=7)
lb5_euro.configure(font=('Mono'))

lb6_btc = Label(aba22, text='Bitcoin: ', background='#3CB371')
lb6_btc.grid(column=2, row=7, columnspan=6, pady=7)
lb6_btc.configure(font=('Mono'))

lb7_info = Label(aba22, text='', background='#3CB371', wraplength=100)
lb7_info.grid(column=2, row=8, pady=5, columnspan=6 )
lb7_info.configure(font=('Bold', 14))
#Final da segunda aba, Aba de calcular

#Terceira aba, aba noticia
lb8 = Label(aba33, text='Última Notícia', background='#4682B4')
lb8.grid(column=0, row=1, pady=34, padx=30)
lb8.configure(font=('Avantgarde', 13))

bt1 = Button(aba33, text='Atualizar', command=noticias)
bt1.grid(column=0, row=0, pady=18, padx=60, ipady=2, ipadx=30)
bt1.configure(font=('FreeMono', 13))

lb9 = Label(aba33, text='...', wraplength=300, justify=CENTER, background='#4682B4')
lb9.grid(column=0, row=2, pady=2)
lb9.configure(font=('Bookman', 15))

lb10 = Label(aba33, text='...', wraplength=300, justify=LEFT, background='#4682B4')
lb10.grid(column=0, row=3, pady=5)
lb10.configure(font=('Courier', 12))
#Final da tereira aba, aba noticia

janela.mainloop()