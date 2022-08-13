import requests
from bs4 import BeautifulSoup
c = 0
while True:
    c += 1
    req = requests.get(f'https://pt.wikipedia.org/wiki/{c}')
    bs = BeautifulSoup(req.content, 'html.parser')
    content = bs.find('div', {'class': 'mw-body-content mw-content-ltr'}).text
    print(f'\r{content}', end='')