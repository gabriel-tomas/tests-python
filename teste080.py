import requests
from bs4 import BeautifulSoup as Bs
from tkinter import *
text = str(input('Input text for traduction: '))
request = requests.get(f'https://www.google.com/search?q=tradutor')
print(request)
bs = Bs(request.text, 'html.parser')
first_input = bs.find_all('span')
print(first_input.find('leite'))
