from tkinter import *
def cotacoes():
    #lista_de_itens = []
    #nomeitem = []
    #precoitem = []
    #while True:
        #lista_de_itens.append(str(input('Digite o nome do item: ')))
        #lista_de_itens.append(float(input('Digite o valor em BRL: R$')))
        #continuar = str(input('Continuar com os valores? [S/N]')).upper()[0]
        #if continuar in 'S':
        #    continue
        #elif continuar in 'N':
        #    break
    import requests
    from bs4 import BeautifulSoup as bs
    requestdolar = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
    requesteuro = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-euro')
    requestbtc = requests.get('https://www.google.com/finance/quote/BTC-BRL?sa=X&ved='
                              '2ahUKEwj1tMup8qT0AhW2r5UCHWBPAvoQ-fUHegQIExAS&window=MAX')
    bsdolar = bs(requestdolar.content, 'html.parser')
    bseuro = bs(requesteuro.content, 'html.parser')
    bsbtc = bs(requestbtc.text, 'html.parser')
    cotacao_dolar = bsdolar.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
    cotacao_euro = bseuro.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
    cotacao_btc = bsbtc.find('div', {'class': 'YMlKec fxKbKc'}).text
    dolar = float(cotacao_dolar.replace(',', '.'))
    euro = float(cotacao_euro.replace(',', '.'))
    btc = float(cotacao_btc.replace(',', ''))
    #for n, itens in enumerate(lista_de_itens):
    #    if n % 2 == 0:
    #        nomeitem.append(itens)
    #    else:
    #        precoitem.append(itens)
    #for n in range(0, len(nomeitem)):
    #    print(f'{nomeitem[n]} com preço R${precoitem[n]}')
    #    print(f'Fica US${precoitem[n] / dolar:.2f} em Dolar')
    #    print(f'Fica EU€{precoitem[n] / euro:.2f} em Euros')
    #    print(f'Fica BTC₿{precoitem[n] / btc:} em Bitcoin')
    dolartext['text'] =f'Dolar: R${dolar}'
    eurotext['text'] = f'Euro: R${euro}'
    btctext['text'] = f'Bitcoin: R${btc}'
    num = convertion.get()
    if bool(num) == False:
        num = 0
    if num == 0 or str(num).isalpha() == True:
        dolartext1['text'] = f'Dolar: R$ 0'
        eurotext2['text'] = f'Euro: R$ 0'
        btctext3['text'] = f'Bitcoin: R$ 0'
    elif num != 0:
        dolartext1['text'] = f'Dolar: R${float(num) * dolar:.2f}'
        eurotext2['text'] = f'Euro: R${float(num) * euro:.2f}'
        btctext3['text'] = f'Bitcoin: R${float(num) * btc:.2f}'

#Interface
janela = Tk()
janela.title('Cotações')
janela.geometry('290x330')

botaoatualizar = Button(janela, text='Atualizar', command=cotacoes)
botaoatualizar.grid(column=1, row=0, pady= 20, padx=80)

dolartext = Label(janela, text='Dolar: ')
dolartext.grid(column=1, row=1, pady=5)

eurotext = Label(janela, text='Euro: ')
eurotext.grid(column=1, row=2, pady=5)

btctext = Label(janela, text='Bitcoin: ')
btctext.grid(column=1, row=3, pady=5)

textR = Label(janela, text='R$')
textR.grid(column=0, row=4, columnspan=1)

convertion = Entry(janela)
convertion.grid(column=1, row=4)

textRe = Label(janela, text='Nas moedas:')
textRe.grid(column=1, row=5)
dolartext1 = Label(janela, text='Dolar: ')
dolartext1.grid(column=1, row=6)

eurotext2 = Label(janela, text='Euro: ')
eurotext2.grid(column=1, row=7)

btctext3 = Label(janela, text='Bitcoin: ')
btctext3.grid(column=1, row=8)

botaosair = Button(janela, text='Sair', command=quit)
botaosair.grid(column=1, row=9, pady=8)

janela.mainloop()