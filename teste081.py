import requests
from bs4 import BeautifulSoup
list_items = []
list_items_search = []
request = requests.get('https://www.mercadolivre.com.br/ofertas?page=1')
bs = BeautifulSoup(request.content, 'html.parser')
for index, paginas in enumerate(bs.find('ul', {'class': 'andes-pagination'})):
    if index == 11:
        num_pages = int(paginas.text)
for pages in range(1, num_pages + 1):
    while True:
        try:
            print(f'\n{"=-" * 20}[ {pages} ]{"-=" * 20}')
            print(f'\033[32m{"CARREGANDO ITENS...":^86}\033[m\n')
            request = requests.get(f'https://www.mercadolivre.com.br/ofertas?page={pages}')
            bs = BeautifulSoup(request.content, 'html.parser')
            for items in bs.find('ol', {'class': 'items_container'}):
                item_name = str(items.find('p', {'class': 'promotion-item__title'}).text).strip()
                if bool((items.find('span', {'class': 'promotion-item__price'})).find('sup')) == True:
                    item_price = ((items.find('span', {'class': 'promotion-item__price'})).find('span').text).replace('R$', '').replace(' ', '')
                    ofi_item_price = ''
                    item_price1 = (items.find('span', {'class': 'promotion-item__price'})).find('sup').text
                    ofi_item_price += item_price.replace('.', '')
                    ofi_item_price += f'.{item_price1}'
                    item_price = float(ofi_item_price)
                    del ofi_item_price
                else:
                    item_price = float(((items.find('span', {'class': 'promotion-item__price'})).find('span').text).replace('R$', '').replace(' ', '').replace('.', ''))
                item_link = str((items.find('a', {'class': 'promotion-item__link-container'})).get('href'))
                item_link_find = item_link.index('JM')
                item_link = item_link[0:item_link_find + 2]
                list_items.append([item_name, item_price, item_link])
                text = f'\r\033[36m{item_name} \033[33m{item_price}\033[m'
                c = 32
                if len(item_name) >= 0:
                    print('\033[35m|', end='')
                    for index, letters in enumerate(item_name):
                        print(f'\033[36m{letters}', end='')
                        if index == c:
                            c += 32
                            print('\n', end='')
                    print('\033[35m|\033[m', end='')
                    print(f'\033[31m|\033[m\033[33m{item_price}\033[31m|\033[m')
                    c = 0
                c1 = 32
                if len(item_link) >= 0:
                    print('\033[31m|', end='')
                    for index, letters in enumerate(item_link):
                        print(f'\033[32m{letters}', end='')
                        if index == c1:
                            c1 += 32
                            print('\n', end='')
                    print('\033[31m|\033[m\n')
            break
        except:
            print(f'\033[31mERRO, TENTANDO NOVAMENTE PÁGINA {pages}\033[m')
index = 0
print(f'\n{"=-" * 19}[ Pesquisa ]{"-=" * 19}\n')
while True:
    list_items_search.clear()
    name_price_user = str(input('Qual item ou preço abaixo você deseja[\033[30mDigite uma palvra chave\033[m]? '))
    while True:
        print('[\033[30mCaso não queira preço minimo e maximo aperte Enter.\033[m]')
        price_max = str(input('Preço maximo: '))
        price_min = str(input('Preço minimo: '))
        if price_max.isnumeric() == True and price_min.isnumeric() == True:
            break
        elif bool(price_max) == False:
            break
        else:
            print('\033[31mErro, digite números\033[m')
    print(f'\n{"=-" * 19}[ Resultado ]{"-=" * 19}')
    for items in list_items:
        if bool(price_max) == True and bool(price_min) == True:
            if name_price_user.isalpha() == True and name_price_user.title() in items[0] and float(price_min) <= items[1] <= float(price_max):
                index += 1
                print(f'{index} - \033[35m{items[0]}\033[m')
                print(f'\033[33mR$ {items[1]}\033[m')
                print(f'\033[32m{items[2]}\033[m\n')
                list_items_search.append([items[0], items[1], items[2]])
        elif name_price_user.isalpha() == True and name_price_user.title() in items[0]:
            index += 1
            print(f'{index} - \033[35m{items[0]}\033[m')
            print(f'\033[33mR$ {items[1]}\033[m')
            print(f'\033[32m{items[2]}\033[m\n')
            list_items_search.append([items[0], items[1], items[2]])
        elif name_price_user.isnumeric() == True and items[1] <= float(name_price_user):
            index += 1
            print(f'{index} - \033[35m{items[0]}\033[m')
            print(f'\033[33mR$ {items[1]}\033[m')
            print(f'\033[32m{items[2]}\033[m\n')
            list_items_search.append([items[0], items[1], items[2]])
    print('[\033[30mCaso não queira ver mais sobre o item aperte Enter.\033[m]')
    more_info = str(input(f'\033[mMostrar mais sobre qual item? [1 até {index}]\033[m '))
    if bool(more_info) == True:
        for index, items in enumerate(list_items_search):
            if index == int(more_info) - 1:
                request_more_info = requests.get(items[2])
                bs_more_info = BeautifulSoup(request_more_info.content, 'html.parser')
                description = bs_more_info.find('p', {'class': 'ui-pdp-description__content'})
        description = str(description).replace('<p class="ui-pdp-description__content">', '').replace('br/>', '').replace('/p>', '')
        print('\033[32m==\033[m' * 40)
        for index, letters in enumerate(description):
            if letters in '<':
                letters = ''
            print(f'\033[33m{letters}\033[m', end='')
            if letters in '<':
                print('\n', end='')
        print('\033[32m==\033[m' * 40)
    index = 0
    see_again = str(input('Nova pesquisa [S/N]? '))
    if see_again in 'Nn':
        break
    print(f'\n{"=-" * 19}[ Resultado ]{"-=" * 19}')
