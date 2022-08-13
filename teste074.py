import requests
from time import sleep
from tkinter import *


def get_zipcode(cod_ras):
    valido = 'N'
    c_verm = 0
    while valido == 'N':
        if c_verm == 0:
            cod_ras = str(input('Digite seu código de rastreamento:\033[m ')).strip().replace('.', '').replace('-', '').upper()
            c_verm += 1
        elif c_verm >= 1:
            cod_ras = str(input('\r\033[31mDigite seu código de rastreamento:\033[m ')).strip().replace('.', '').replace('-', '').upper()
        if len(cod_ras) == 13:
            valido = 'S'
            return cod_ras
        else:
            print('\033[1mCódigo inválido\033[m')
            valido = 'N'
codigo_rastreamento = get_zipcode(0)
def eventos(cod_json):
    c = 0
    while True:
        request = requests.get(f'https://api.linketrack.com/track/json?user=teste&token=1abcd00b2731640e886fb41a8a9671ad1434c599dbaa0a0de9a5aa619f29a83f&codigo={codigo_rastreamento}')
        sleep(1)
        c += 1
        print(f'\r\033[35mBuscando...{c}\033[m', end='')
        if request.status_code == 200:
            json = request.json()
            cod_json = json['eventos']
            print('\n\n\033[36mStatus da encomenda:\033[m\n')
            c = 1
            if bool(json['eventos']) == False:
                print('\033[1;34mEncomenda NÃO encontrada, ou foi postada\nrecentemente e não pode ser vista\033[m\n')
                break
            return cod_json
evento_all = eventos(0)
if bool(evento_all):
    def status():
        listastatus = []
        listalocal = []
        listadata = []
        listahora = []
        listasubstatus = []
        c = 1
        for evento in evento_all:
            status = f'\033[3{c}mStatus: \033[1m{evento["status"]}\033[m'
            local = f'\033[3{c}mLocal: {evento["local"]}'
            data = f'Data: {evento["data"]}'
            hora = f'Hora: {evento["hora"]}'
            listastatus.append(status)
            listalocal.append(local)
            listadata.append(data)
            listahora.append(hora)
            if bool(evento['subStatus']) == True and str(evento['subStatus']).find('<') <= 0:
                substatus = f'Status adicional: {evento["subStatus"][0]}'
            elif str(evento['subStatus']).find('<') >= 0:
                str_substatus0 = str(evento['subStatus'][0])
                index1 = [str_substatus0.index('='),
                str_substatus0.index('>'),
                str_substatus0[1:].index('<')]
                substatus = f'Status adicional: {str_substatus0[index1[1]+1:index1[2]]} {str_substatus0[index1[0]+2: index1[1]-1]}\033[m'
            else:
                substatus = 'N/A'
            listasubstatus.append(substatus)
            c += 1
        for n in range(0, len(listastatus)):
            print(f'{listastatus[n]}\n{listalocal[n]}\n{listadata[n]}\n{listahora[n]}\n{listasubstatus[n]}\n')
    status()