n = int(input('Número inteiro: '))
par = n % 2 == 0
if par:
    print('Paia')
    a = input('Quer saber o segredo? ')
    if a.isalpha():
        input('se for par {} resto da divisão por 2 = {}'.format(n, n % 2))
else:
    print('Impaia')

