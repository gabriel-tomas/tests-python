from random import choice
from time import sleep
print('Jogo da forca')
print('''Você tem 3 vidas''')
lista = ['Macaco', 'Violão', 'Pizza']
escolha = choice(lista)
if escolha == 'Macaco':
    dus = 'k'
    vidas = 3
    while dus != 'M':
        dus = str(input('Digite: '))
        if dus != 'M':
            vidas = vidas - 1
        if vidas == 0:
            quit('VOCÊ PERDEU')
    print('M')
    while dus != 'a':
        dus = str(input('Digite: '))
        if dus != 'a':
            vidas = vidas - 1
        if vidas == 0:
            quit('VOCÊ PERDEU')
    print('Ma')
    while dus != 'c':
        dus = str(input('Digite:'))
        if dus != 'c':
            vidas = vidas - 1
        if vidas == 0:
            quit('VOCÊ PERDEU')
    print('Maca')
    while dus != 'a':
        dus = str(input('Digite: '))
        if dus != 'a':
            vidas = vidas - 1
        if vidas == 0:
            quit('VOCÊ PERDEU')
    print('Maca')
    while dus != 'c':
        dus = str(input('Digite:'))
        if dus != 'c':
            vidas = vidas - 1
        if vidas == 0:
            quit('VOCÊ PERDEU')
    print('Macac')
    while dus != 'o':
        dus = str(input('Digite: '))
        if dus != 'o':
            vidas = vidas - 1
        if vidas == 0:
            quit('VOCÊ PERDEU')
    print('\033[33mParabéns')
    sleep(2)
    print('\033[32mVOCÊ GANHOU!\033[m')
    sleep(1)
    print('\033[37mA resposta era: \033[1;4mMacaco')
if escolha == 'Violão':
    dus = 'k'
    vidas = 3
    while dus != 'V':
        dus = str(input('Digite: '))
        if dus != 'V':
            vidas = vidas - 1
        if vidas == 0:
            quit('VOCÊ PERDEU')
    print('V')
