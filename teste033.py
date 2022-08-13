n = str(input('Digite um número com ponto flutuante: '))
a = n.split('.')
print('Parte inteira é {} e a depois do ponto flutuante, ou vírgula, é {}'.format(a[0], a[1]))
