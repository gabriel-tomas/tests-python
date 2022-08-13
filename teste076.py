import requests
from bs4 import BeautifulSoup
item = str(input('O que você quer saber? '))
request = requests.get(f'https://www.bing.com/search?q={item}+conceito')
bs = BeautifulSoup(request.content, 'html.parser')
conteudo = bs.find('', {'class': ''})