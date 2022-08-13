import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from datetime import date
def req_itens():
    rq_quant_paginas = requests.get('https://www.mercadolivre.com.br/ofertas?promotion_type=LIGHTNING_DEAL&page=1')
    bs_quant_paginas = BeautifulSoup(rq_quant_paginas.content, 'html.parser')
    page1 = bs_quant_paginas.find('ul', {'class':'andes-pagination'})
    enum = len(page1)
    for n, pages in enumerate(page1):
        num = pages.text
        if n == enum-2:
            break
    num = int(num)
    print(num)
    num_itens_tot = 0
    c = 0
    for paginas in range(1, num+1):
        request = requests.get(f'https://www.mercadolivre.com.br/ofertas?promotion_type=LIGHTNING_DEAL&page={paginas}')
        bs = BeautifulSoup(request.content, 'html.parser')
        container_itens = bs.find('ol', {'class': 'items_container'})
        print(f'\033[33mPágina {paginas}\033[m')
        for nome_preco_desconto in container_itens:
            num_itens_tot += 1
            nome = nome_preco_desconto.find('p', {'class': 'promotion-item__title'}).text
            preco = nome_preco_desconto.find('span', {'class': 'promotion-item__price'}).text
            if bool(nome_preco_desconto.find('div', {'class': 'promotion-item__price-additional-info'}).text) == True:
                desconto = nome_preco_desconto.find('div', {'class': 'promotion-item__price-additional-info'}).text
            else:
                desconto = '0%'
            nome_item = f'Nome: {nome}'
            preco_item = f'Preço:{preco}'
            desconto_item = f'Desconto: {desconto}'
            with open(f'itens {date.today()}.txt', 'a+') as item:
                c += 1
                item.write(f'Item {c}:\n')
                item.write(f'Nome: {nome}\n')
                item.write(f'Preço:{preco}\n')
                item.write(f'Desconto: {desconto}\n\n')    
    lb3['text'] = f'Toal de {num_itens_tot} itens'
janela_main = Tk()
janela_main.geometry('210x260')
janela_main.configure(background='#FFD700')
janela_main.title('Ofertas Relampago')

lb1 = Label(janela_main, text='Itens Oferta')
lb1.grid(column=0, row=0, padx=35, pady=20)
lb1.configure(font=('Avantgarde', 18), background='#FFD700')

bt1 = Button(janela_main, text='Criar arquivo', command=req_itens)
bt1.grid(column=0, row=1, pady=15)
bt1.configure(font=('Courier New', 10))

lb3 = Label(janela_main, text=f'Total de ... itens')
lb3.grid(column=0, row=2)
lb3.configure(font=('Avantgarde', 11), background='#FFD700')

lb2 = Label(janela_main, text=f'Data de hoje: {date.today()}')
lb2.grid(column=0, row=3, pady=23)
lb2.configure(font=('Avantgarde', 11), background='#FFD700')

btdestroy = Button(janela_main, text='Sair', command=janela_main.destroy)
btdestroy.grid(column=0, row=4, pady=5)
btdestroy.configure(font=('Courier New', 10))

janela_main.mainloop()
