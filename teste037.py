nomevelho = ''
nomenovo = ''
idade1 = 0
idade2 = 0
for co in range(1, 4):
    atleta = str(input('Nome do {} atleta: '.format(co)))
    idade = int(input('Idade do {} atleta: '.format(co)))
    if co == 1:
        nomevelho = atleta
        idade1 = idade
    if idade > idade1:
        nomevelho = atleta
        idade1 = idade
    if co == 1:
        nomenovo = atleta
        idade2 = idade
    if idade < idade2:
        nomenovo = atleta
        idade2 = idade
print('O atleta mais velho é {} com {} de idade'.format(nomevelho, idade1))
print('O atleta mais novo é {} com {} de idade'.format(nomenovo, idade2))
