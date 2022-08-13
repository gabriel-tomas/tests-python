import requests
from bs4 import BeautifulSoup
from datetime import date
import pyautogui
import requests
def mercadolivre():
    listadeitens = []
    listadeitenslink = []
    listadepreco = []
    listadedesconto = []
    maiordesconto = menordesconto = 0
    nomedomaiordesconto = nomedomenordesconto = ''
    linkdomaiordesconto = linkdomenordesconto = ''
    request = requests.get('https://www.mercadolivre.com.br/ofertas#nav-header')
    site = BeautifulSoup(request.content, 'html.parser')
    itens = site.find('ol', {'class': 'items_container'})
    print('Itens do dia:')
    for n, cadaitem in enumerate(itens):
        preco = cadaitem.find('span', {'class': 'promotion-item__price'}).text
        desconto = cadaitem.find('span', {'class': 'promotion-item__discount'})
        cadaitem1 = str(cadaitem).index('href')
        a1 = str(cadaitem).find('_JM')
        a2 = str(cadaitem)[cadaitem1:a1].replace('-', ' ')
        a3 = a2.split()[2:]
        a4 = ' '.join(a3)
        produtos = f'Produto {n+1}: \033[30:47m{a4}\033[m'
        print(produtos)
        print(f'Preço: {preco}')
        listadepreco.append(preco)
        desconto1 = str(desconto)[39:41].replace("<", "")
        b1 = str(cadaitem)[cadaitem1 + 6:a1 + 3]
        if desconto1 == '':
            desconto1 = '0'
        if n == 0 or int(desconto1) > maiordesconto:
            maiordesconto = int(desconto1)
            nomedomaiordesconto = a4
            linkdomaiordesconto = b1
        if n == 0 or int(desconto1) < menordesconto:
            menordesconto = int(desconto1)
            nomedomenordesconto = a4
            linkdomenordesconto = b1
        print(f'Desconto: {desconto1}% OFF')
        listadedesconto.append(desconto1)
        listadeitens.append(a4)
        listadeitenslink.append(b1)
        print(f'Link: {b1}\n')
    print(f'O maior desconto é do produto: {nomedomaiordesconto}\n'
          f'Desconto: {maiordesconto}%'
          f'Link: {linkdomaiordesconto}'
          f'\nE o menor é do produto: {nomedomenordesconto}\n'
          f'Desconto: {menordesconto}%'
          f'Link: {linkdomenordesconto}\n')
    print(f'Hoje é: {date.today().day}')
    with open(f'Produtos {date.today()}.html', 'a+') as texto:
        texto.write(f'<h2>Data atual: {date.today()}</h2>\n')
        for cadaproduto in range(0, len(listadeitens)):
            texto.write(f'<head> <title>Itens mercadolivre</title><head>'
                        f'<body><li>Produto: {listadeitens[cadaproduto]}</li>\n')
            texto.write(f'<p>Preco: {listadepreco[cadaproduto]}</p>\n')
            texto.write(f'<p>Desconto: {listadedesconto[cadaproduto]}% OFF</p>\n')
            texto.write(f'<a href={listadeitenslink[cadaproduto]}>Link do produto {cadaproduto}</a>\n')
        texto.write(f'''<p>O produto com *maior desconto*: {nomedomaiordesconto}</p>
<p>Com desconto de: {maiordesconto}%</p>
<p>Link: {linkdomaiordesconto}</p>
<p>O produto com *menor desconto*: {nomedomenordesconto}</p>
<p>Com desconto de: {menordesconto}%</p>
<p>Link: {linkdomenordesconto}</p></body>''')
    with open(f'Site mercadoitens.html', 'a+') as aditens:
        aditens.write(f'<h4>Itens do dia: {date.today()}</h4>')
        aditens.write(f'<li><a href=http://localhost:63342/Testes/Produtos%20{date.today()}.html?_ijt=hhmnfcj051l6p1gna3lfcueggk&_ij_reload=RELOAD_ON_SAVE>Aqui</a></li>\n')
mercadolivre()
