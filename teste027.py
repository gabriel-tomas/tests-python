from random import randint
from time import sleep
a = randint(0, 10)
print('Pensando num número...')
sleep(3)
p = int(input('Digite um valor: '))
if p == a:
    print('VENCEU!')
if p > a:
    print('Mais para baixo')
if p < a:
    print('Mais para cima')
if p < a or p > a:
    while(1):
        p = int(input('Digite um valor: '))
        if p == randint(0, 10):
            quit('VENCEU!')
        if p > randint(0, 10):
            print('Mais para baixo')
        if p < randint(0, 10):
            print('Mais para cima')
