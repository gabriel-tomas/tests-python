nome = str(input('Digite seu nome: '))
n_separado = nome.split()
n1 = n_separado[0]
n2 = n_separado[1:]
print('Primeiro nome é {}\nSobrenome é {}'.format(n1, ' '.join(n2)))
