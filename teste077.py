import requests
from tkinter import *
def cep():
    cep = entry_cep.get()
    if bool(cep) == True:
        try:
            request = requests.get(f'https://ws.apicep.com/cep/{cep}.json')
            requestjson = request.json()
            text_state['text'] = requestjson['state']
            text_city['text'] = requestjson['city']
            text_district['text'] = requestjson['district']
            text_address['text'] = requestjson['address']
            if requestjson['statusText'] == 'bad_request':
                while True:
                    request = requests.get(f'https://ws.apicep.com/cep/{cep}.json')
                    requestjson = request.json()
                    if requestjson['statusText'] == 'ok':
                        break
        except:
            text_state['text'] = 'Estado: Error'
            text_city['text'] = 'Cidade: Error'
            text_district['text'] = 'Distrito: Error'
            text_address['text'] = 'Endereço: Error'
    else:
        text_state['text'] = 'Estado: Error'
        text_city['text'] = 'Cidade: Error'
        text_district['text'] = 'Distrito: Error'
        text_address['text'] = 'Endereço: Error'

window = Tk()
button_start = Button(window, text='Find', command=cep)
button_start.grid(column=0, row=1)
entry_cep = Entry(window)
entry_cep.grid(column=0, row=0)
text_state = Label(window, text='Estado: ', wraplength=180)
text_state.grid(column=0, row=2)
text_city = Label(window, text='Cidade: ', wraplength=180)
text_city.grid(column=0, row=3)
text_district = Label(window, text='Distrito: ', wraplength=180)
text_district.grid(column=0, row=4)
text_address = Label(window, text='Endereço: ', wraplength=180)
text_address.grid(column=0, row=5)
window.mainloop()
