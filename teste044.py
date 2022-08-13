from time import sleep
opc = ''
t1 = 0
while opc != 'x':
    opc = str(input('(Para sair digite "x")\nSegundo ou minuto? [s/m]')).lower()
    if opc == 's':
        t1 = int(input('Quantos segundos? '))
    elif opc == 'm':
        t1 = int(input('Quantos minutos? '))
    elif opc == 'x':
        sair = 'Saindo do programa'
        for c in range(0, 4):
            if c == 0:
                print('{}'.format(sair), end='')
            if c == 1:
                print('.'.format(sair), end='')
            if c == 2:
                print('.'.format(sair), end='')
            if c == 3:
                print('.'.format(sair))
            sleep(1)
    else:
        print('OPÇÃO INVÁLIDA')
    contador = 0
    if opc == 's':
        while t1 != 0:
            print(t1, end=' ')
            contador = contador + 1
            if contador == 5:
                print('\n')
                contador = contador - contador
            t1 = t1 - 1
            sleep(1)
    elif opc == 'm':
        cat1 = t1 * 60
        while cat1 != 0:
            contador = contador + 1
            print(cat1, end=' ')
            if contador == 5:
                print('\n')
                contador = contador - contador
            cat1 = cat1 - 1
            sleep(1)
