from time import sleep
n = int(input('Digite quantos minutos vai o contador: '))
nc = n*60
sleep(nc)
print('Passaram {} minutos que é {} segundos'.format(n, nc))
