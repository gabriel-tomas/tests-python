def cotaatuais():
    dolaratual = euroatual = btcatual = c = 0
    while True:
        import requests
        from bs4 import BeautifulSoup as bs
        requestdolar = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
        requesteuro = requests.get('https://www.remessaonline.com.br/cotacao/cotacao-euro')
        requestbtc = requests.get('https://www.google.com/finance/quote/BTC-BRL?sa=X&ved=2ahUKEwj1tMup8qT0AhW2r5UCHWBPAvoQ-fUHegQIExAS&window=MAX')
        bsdolar = bs(requestdolar.content, 'html.parser')
        bseuro = bs(requesteuro.content, 'html.parser')
        bsbtc = bs(requestbtc.text, 'html.parser')
        cotacao_dolar = bsdolar.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
        cotacao_euro = bseuro.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
        cotacao_btc = bsbtc.find('div', {'class': 'YMlKec fxKbKc'}).text
        dolar = float(cotacao_dolar.replace(',', '.'))
        euro = float(cotacao_euro.replace(',', '.'))
        btc = float(cotacao_btc.replace(',', ''))
        if c == 1 or dolar > dolaratual:
            dolaratual = dolar
            print(f'Dolar: R$ {dolaratual}')
        if c == 1 or dolar < dolaratual:
            dolaratual = dolar
            print(f'Dolar: R$ {dolaratual}')
        if c == 1 or euro > euroatual:
            euroatual = euro
            print(f'Euro: R$ {euroatual}')
        if c == 1 or euro < euroatual:
            euroatual = euro
            print(f'Euro: R$ {euroatual}')
        if c == 1 or btc > btcatual:
            btcatual = btc
            print(f'Bitcoin: R$ {btcatual}')
        if c == 1 or btc < btcatual:
            btcatual = btc
            print(f'Bitcoin: R$ {btcatual}')
cotaatuais()
