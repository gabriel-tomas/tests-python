nome = str(input('Nome: '))
print('{} tem {} letras, '.format(nome, len(nome)), end='')
print('Tem {} "a" '.format(nome.lower().count('a')), end='')
print('e tem {} vogais'.format(nome.count('a') + nome.count('e') + nome.count('i') +
                             nome.count('o') + nome.count('u')))
