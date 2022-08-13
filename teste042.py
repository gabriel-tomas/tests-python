import random
lista = [1, 2, 3]
ran = random.choice(lista)
print('Escolha entre 1 e 3')
es = int(input('Digite sua jogada: '))
while ran != es:
    es = int(input('Digite sua jogada: '))
    ran = random.choice(lista)
if ran == es:
    print('A escolha foi igual')
