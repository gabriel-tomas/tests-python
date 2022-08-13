p = input('Você gostaria de jogar o dado? ').lower()
from random import randint
if p == 'sim':
    print(randint(0, 10))
p1 = input('Quer ver novamente? ').lower()
if p1 == 'sim':
    print(randint(0, 10))
    while(1):
        p = input('Novamente? ').lower()
        if p == 'sim':
            print(randint(0, 10))
        if p == 'não':
            quit('Saindo...')
if p1 == 'não':
    quit('Saindo...')
    