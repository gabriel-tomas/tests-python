import time, random
for tempo in range(1, 5):
    lista = ['cachorro', 'gato', 'papagaio', 'tatu']
    rand = random.choice(lista)
    time.sleep(1)
    if tempo == 1:
        print(rand)
    if tempo == 2:
        print(rand)
    if tempo == 3:
        print(rand)
    if tempo == 4:
        print(rand)
    if tempo == 5:
        print(rand)
for tempinho in range(1, 9999):
    lista = [3, 4, 6, 7, 9, 23, 43]
    rand = random.randint(3, 43)
    rand2 = random.choice(lista)
    print('{}X{}={:>1}'.format(rand, rand2, rand**rand2))
