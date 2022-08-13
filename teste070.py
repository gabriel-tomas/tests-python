from bs4 import BeautifulSoup as Bs
import requests
from tkinter import *
def pesquisa(): #req google pesquisa
    try:
        pesq = ent1.get()
        request = requests.get(f'https://pt.wikipedia.org/wiki/{pesq}')
        bs4 = Bs(request.content, 'html.parser')
        resultado = bs4.find('div', {'class': 'mw-parser-output'})
        resultadoparagraf = resultado.find('p').text
        resultadotextatefp = str(resultadoparagraf).find('.')
        print(bool(resultadoparagraf))
        resultado_final = resultadoparagraf[0:resultadotextatefp+1]
        if resultadotextatefp <= -1:
            text1['text'] = f'Não foi possível encontrar'
        elif resultadotextatefp >= 1:
            text1['text'] = resultado_final
    except:
        text1['text'] = f'Não foi possível encontrar'
#janela infos
janela = Tk()
win_width= 230
But1 = Button(janela, text='Pesquisar', command=pesquisa).grid(column=0, row=0)
ent1 = Entry(janela)
ent1.grid(column=0, row=1, sticky=W, padx=23)
text1 = Label(janela, text='Nenhuma pesquisa', wraplength=win_width)
text1.grid(column=0, row=2, sticky=W)
quit = Button(janela, text='Sair', command=janela.destroy)
quit.grid(column=0, row=3, pady=4)
janela.mainloop()
