from tkinter import *
import requests
from bs4 import BeautifulSoup
def cotacao():
    valor = requests.get('https://valor.globo.com/valor-data/')
    bs = BeautifulSoup(valor.content, 'html.parser')
    cotdolar = bs.find('div', {'class': 'cell auto data-cotacao__ticker_quote'}).text
    pordolar = bs.find('div', {'class': 'cell auto data-cotacao__ticker_percentage_green'}).text
    textfinfo2['text'] = f'A cotação atual do dolar: {cotdolar}\ncom aumento de{pordolar}'
Janela = Tk()

textinfo1 = Label(Janela, text='Cotação do Dolar')
textinfo1.grid(column=0, row=0)
botaoinfo = Label(Janela, text='Para atualizar clique no Botão abaixo')
botaoinfo.grid(column=0, row=1)
botaoiniciar = Button(Janela, text='Atualizar', command=cotacao)
botaoiniciar.grid(column=0, row=2)
textfinfo2 = Label(Janela, text='')
textfinfo2.grid(column=0, row=3)
Janela.mainloop()

