print('''Opções:
1...............Calculadora
2...............Saque
3...............Lista de produtos
4...............Sair''')
op = 5
nt = ntb = contcem = contcinquenta = contvinte = contdez = contcinco = contdois = contum = 0
a = sinal = ''
while op > 4:
    op = int(input('Digite: '))
    if op == 1:
        print('=' * 10, 'Calculadora', '=' * 10)
        while True:
            n = str(input('')).strip()
            if n.isalpha() == True:
                break
            if n.find('+') != -1:
                a = n.split('+')
                sinal = '+'
            elif n.find('-') != -1:
                a = n.split('-')
                sinal = '-'
            elif n.find('x') != -1:
                a = n.split('x')
                sinal = 'x'
            if n.find(sinal) != -1:
                for sn in range(0, len(a)):
                    if a[sn].isnumeric() == True or a[sn].find('.') == True:
                        n = float(a[sn])
                        if sinal == '+':
                            nt += n
                        elif sinal == '-':
                            nt -= n
                        elif sinal == 'x':
                            nt *= n
                print(nt, end='')
    elif op == 2:
        nb = int(input('Digite quanto quer sacar: R$'))
        ntb = nb
        while ntb - 100 >= 0:
            ntb -= 100
            contcem += 1
        if contcem >= 1:
            print(f'{contcem} Notas de R$100')
        while ntb - 50 >= 0:
            ntb -= 50
            contcinquenta += 1
        if contcinquenta >= 1:
            print(f'{contcinquenta:} Notas de R$50')
        while ntb - 20 >= 0:
            ntb -= 20
            contvinte += 1
        if contvinte >= 1:
            print(f'{contvinte} Notas de R$20')
        while ntb - 10 >= 0:
            ntb -= 10
            contdez += 1
        if contdez >= 1:
            print(f'{contdez} Notas de R$10')
        while ntb - 5 >= 0:
            ntb -= 5
            contcinco += 1
        if contcinco >= 1:
            print(f'{contcinco} Notas de R$5')
        while ntb - 2 >= 0:
            ntb -= 2
            contdois += 1
        if contdois >= 1:
            print(f'{contdois} Notas de R$2')
        while ntb - 1 >= 0:
            ntb -= 1
            contum += 1
        if contum >= 1:
            print(f'{contum} Moedas de R$1')
    elif op == 3:
        itens = (str(input('Digite o item um: ')),
                str(input('Digite o preço do item um:')),
                str(input('Digite o item dois:')),
                str(input('Digite o preço do item dois:')),
                str(input('Digite o item três:')),
                str(input('Digite o preço do item três:')),
                str(input('Digite o item quatro:')),
                str(input('Digite o preço do item quatro:')),
                str(input('Digite o item cinco:')),
                str(input('Digite o preço do item cinco: ')))
        print('=' * 20, end='')
        print('LISTA', end='')
        print('=' * 20)
        for item in range(0, len(itens)):
            if item % 2 != 0:
                print(f'{"R$" + itens[item]:.>15}')
            else:
                print(f'{itens[item]:.<10}{"." * 17}', end='')
