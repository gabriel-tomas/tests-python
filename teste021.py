import random
p = input('Randomizar? ').lower()
if p == 'sim':
    s = random.randint(1, 3)
    print(s)
    if s == 1:
        P = int(input('Qual a raiz de 81? '))
        if P == 9:
           print('Acertou!')
    if s == 2:
        p2 = int(input('8x2? '))
        if p2 == 16:
           print('Acertou!')
    if s == 3:
        p3 = input('Diga seu nome: ')
        print('Olá {}'.format(p3))



