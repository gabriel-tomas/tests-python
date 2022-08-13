import requests
from bs4 import BeautifulSoup
from tkinter import *
def iniciar_busca_cep():
    cep = entrada_cep.get().replace('-', '').replace('.', '').replace(' ', '')
    if bool(cep) == True:
        try:
            request = requests.get(f'http://cep.la/{cep}')
            site = BeautifulSoup(request.content, 'html.parser')
            end = site.find('div', {'id': 'main'})
            end_tratamento1 = str(end).index('<div id="an">')
            end_tratamento2 = str(end).index('>')
            end_tratamento3 = str(end)[end_tratamento2 + 1:end_tratamento1]
            end_tratamento4 = end_tratamento3.split()[6:]
            end_tratamento5 = ' '.join(end_tratamento4).split(',')
            rua = end_tratamento5[0]
            distrito = end_tratamento5[1][1:]
            municipio1 = end_tratamento5[2].index('-')
            municipio = end_tratamento5[2][1:municipio1]
            estado = end_tratamento5[2][municipio1 + 2:]
            texto_rua['text'] =f'Rua: {rua}'
            texto_distrito['text'] =f'Distrito: {distrito}'
            texto_municipio['text'] =f'Município: {municipio}'
            texto_estado['text'] =f'Estado: {estado}'
        except:
            texto_rua['text'] = f'Rua: Cep não encontrado'
            texto_distrito['text'] = f'Distrito: Cep não encontrado'
            texto_municipio['text'] = f'Município: Cep não encontrado'
            texto_estado['text'] = f'Estado: Cep não encontrado'
    else:
        texto_rua['text'] = f'Rua: N/A'
        texto_distrito['text'] = f'Distrito: N/A'
        texto_municipio['text'] = f'Município: N/A'
        texto_estado['text'] = f'Estado: N/A'
jnl = Tk()
jnl.title('Busca CEP')
info_cep = Label(jnl, text='Cep:')
info_cep.grid(column=0, row=0)

entrada_cep = Entry(jnl)
entrada_cep.grid(column=1, row=0, pady=23)

botao_buscas = Button(jnl, text='Buscar', command=iniciar_busca_cep)
botao_buscas.grid(column=2, row=0)

botao_sair = Button(jnl, text='Sair', command=jnl.destroy)
botao_sair.grid(column=2, row=5)

texto_rua = Label(jnl, text='Rua:')
texto_rua.grid(column=1, row=2, pady=9)

texto_distrito = Label(jnl, text='Distrito: ')
texto_distrito.grid(column=1, row=3, pady=9)

texto_municipio = Label(jnl, text='Município: ')
texto_municipio.grid(column=1, row=4, pady=9)

texto_estado = Label(jnl, text='Bairro: ')
texto_estado.grid(column=1, row=5, pady=9)

jnl.mainloop()
