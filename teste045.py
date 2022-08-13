sac = int(input('Quanto dinheiro quer sacar? R$'))
print('''[ 1 ] Para só notas de R$100
[ 2 ] Para só notas de R$50
[ 3 ] Para só notas de R$20
[ 4 ] Para só notas de R$10
[ 5 ] Para só notas de R$5
[ 6 ] Para só notas de R$2
Digite "0" para quantidades exatas''')
notastot = ''
while True:
    notas = str(input('Existe notas apenas de quanto? '))
    notastot = notastot, notas
    continuar = str(input('Mais alguma [S/N]? ')).upper()
    if continuar == 'N':
        break
print(notastot)
contcem = 0
contcinquenta = 0
contvinte = 0
contdez = 0
contcinco = 0
contdois = 0
contum = 0
if notas == 1 or notas == 0:
    while True:
        if sac - 100 < 0:
            break
        sac -= 100
        contcem += 1
    print(f'{contcem} Notas de R$100')
    if notas == 1:
        print(f'Restou R${sac}')
        quit()
if notas == 2 or notas == 0:
    while True:
        if sac - 50 < 0:
            break
        sac -= 50
        contcinquenta += 1
    print(f'{contcinquenta} Notas de R$50')
    if notas == 2:
        print(f'Restou R${sac}')
        quit()
if notas == 3 or notas == 0:
    while True:
        if sac - 20 < 0:
            break
        sac -= 20
        contvinte += 1
    print(f'{contvinte} Notas de R$20')
    if notas == 3:
        print(f'Restou R${sac}')
        quit()
if notas == 4 or notas == 0:
    while True:
        if sac - 10 < 0:
            break
        sac -= 10
        contdez += 1
    print(f'{contdez} Notas de R$10')
    if notas == 4:
        print(f'Restou R${sac}')
        quit()
if notas == 5 or notas == 0:
    while True:
        if sac - 5 < 0:
            break
        sac -= 5
        contcinco += 1
    print(f'{contcinco} Notas de R$5')
    if notas == 5:
        print(f'Restou R${sac}')
        quit()
if notas == 6 or notas == 0:
    while True:
        if sac - 2 < 0:
            break
        sac -= 2
        contdois += 1
    print(f'{contdois} Notas de R$2')
    if notas == 6:
        print(f'Restou R${sac}')
        quit()
while True:
    if sac - 1 < 0:
        break
    sac -= 1
    contum += 1
print(f'{contum} Moedas de R$1' if contum > 1 else f'{contum} Moeda de R$1')
