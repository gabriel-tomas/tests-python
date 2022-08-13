pessoa1 = pessoa2 = pessoa3 = ''
idade1 = idade2 = idade3 = 0
for c in range(1, 4):
    pessoa = str(input('Nome: '))
    idade = int(input('Idade: '))
    if c == 1:
        pessoa1 = pessoa
        idade1 = idade
    if c == 2:
        pessoa2 = pessoa
        idade2 = idade
    if c == 3:
        pessoa3 = pessoa
        idade3 =idade
print(f'Temos o {pessoa1} com {idade1}'
      f'\n{pessoa2} com {idade2}'
      f'\n{pessoa3} com {idade3}')