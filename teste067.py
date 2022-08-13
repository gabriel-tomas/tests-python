from bs4 import BeautifulSoup
from datetime import date
import requests
request_paginas = requests.get('https://www.mercadolivre.com.br/ofertas?page=1')
bs4 = BeautifulSoup(request_paginas.content, 'html.parser')
num_paginasbs = bs4.find('ul', {'class': 'andes-pagination'}).text
num_paginas = int(num_paginasbs[17:20])
try:
    ntot_itens = 0
    lista_nomes = []
    lista_precos = []
    lista_links = []
    lista_paginas = []
    lista_num_produtos = []
    lista_descontos = []
    for page in range(1, num_paginas+1):
        request = requests.get(f'https://www.mercadolivre.com.br/ofertas?page={page}')
        bspage = BeautifulSoup(request.content, 'html.parser')
        if str(request).find('200') == 11:
            itens = bspage.find('ol', {'class': 'items_container'})
            for n, item in enumerate(itens):
                ntot_itens += 1
                item_nome = item.find('p', {'class': 'promotion-item__title'}).text
                item_preco = item.find('span', {'class': 'promotion-item__price'}).text
                item_link = str(item.find('a', {'class': 'promotion-item__link-container'}))
                item_link_tratamento1 = str(item_link).index('href')
                item_link_tratamento2 = str(item_link).index('_JM')
                item_link_tratamento3 = str(item_link)[item_link_tratamento1 + 6:item_link_tratamento2 + 3]
                item_desconto = item.find('div', {'class': 'promotion-item__price-additional-info'})
                item_desconto1 = item_desconto.find('span', {'class': 'promotion-item__discount'})
                if bool(item_desconto1) == False:
                    item_desconto2 = 0
                    lista_descontos.append(item_desconto2)
                else:
                    item_desconto2 = str(item_desconto.find('span', {'class': 'promotion-item__discount'}).text)[0:2].replace('%', '')
                    lista_descontos.append(item_desconto2)
                nome_final = item_nome.strip()
                preco_final = item_preco
                link_final = item_link_tratamento3
                lista_nomes.append(nome_final)
                lista_precos.append(preco_final)
                lista_links.append(link_final)
                print(f'Nome:{nome_final}')
                print(f'Preço: {preco_final}')
                print(f'Desconto: {item_desconto2}%\n')
            pagina = f'Pagina: {page}'
            num_total_itens_paginas = f'Numéro de itens: {ntot_itens}'
            lista_paginas.append(pagina)
            print(pagina)
            print(num_total_itens_paginas)
    with open(f'Produtos {date.today()}.html', 'a+') as texto:
        texto.write('<head><meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> </head>')
        texto.write('<body>')
        texto.write(f'<h2>Data atual: {date.today()}</h2>\n')
        texto.write(f'<h3>Total de {len(lista_paginas)} paginas</h3>')
        texto.write(f'<h4>Total de {ntot_itens} itens</h4>')
        for num_lista_itens in range(0, len(lista_precos)):
            texto.write(f'<li>Nome do item: {lista_nomes[num_lista_itens]}</li>\n')
            texto.write(f'<p>Preco do item: {lista_precos[num_lista_itens]}</p>')
            texto.write(f'<p>Desconto: {lista_descontos[num_lista_itens]}%<a href={lista_links[num_lista_itens]}> Link</a></p>')
            texto.write(f'<br> </br>')
            texto.write('</body>')
    with open(f'Ofertas do dia.html', 'a+') as Ofertas:
        Ofertas.write(f'''  <div class=Itens1>
        <p>Item do dia {date.today()}</p>\n''')
        Ofertas.write(f'''      <a href=http://localhost:63342/Testes/Produtos%20{date.today()}.html?_ijt=396vbn3hkb8c3tdt68r1s84icb&_ij_reload=RELOAD_ON_SAVE>Aqui</a>
  </div>''')
except:
    print('Erro, naõ foi possivel acessar o site')
