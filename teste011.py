n1 = input('')
sinal = input('{}'.format(n1))
n2 = input('{}{}'.format(n1, sinal))
if sinal == '+':
    print('{}{}{}={}'.format(n1, sinal, n2, (float(n1)+float(n2))))
    resultado = (float(n1)+float(n2))
    sinal3 = input('{}'.format(resultado))
    n3 = input('{}{}'.format(resultado, sinal3))
    if sinal3 == '+':
        print('{}{}{}={}'.format(resultado, sinal3, n3, (float(resultado)+float(n3))))
    if sinal3 == '-':
        print('{}{}{}={}'.format(resultado, sinal3, n3, (float(resultado)-float(n3))))
    if sinal3 == 'x':
        print('{}{}{}={}'.format(resultado, sinal3, n3, (float(resultado)*float(n3))))
if sinal == '-':
    print('{}{}{}={}'.format(n1, sinal, n2, (float(n1)-float(n2))))
    resultado2 = (float(n1)-float(n2))
    sinal3 = input('{}'.format(resultado2))
    n3 = input('{}{}'.format(resultado2, sinal3))
    if sinal3 == '-':
        print('{}{}{}={}'.format(resultado2, sinal3, n3, (float(resultado2)-float(n3))))
    if sinal3 == '+':
        print('{}{}{}={}'.format(resultado2, sinal3, n3, (float(resultado2)+float(n3))))
    if sinal3 == 'x':
        print('{}{}{}={}'.format(resultado2, sinal3, n3, (float(resultado2)*float(n3))))
if sinal == 'x':
    print('{}{}{}={}'.format(n1, sinal, n2, (float(n1)*float(n2))))
    resultado3 = (float(n1)*float(n2))
    sinal3 = input(resultado3)
    n3 = input('{}{}'.format(resultado3, sinal3))
    if sinal3 == 'x':
        print('{}{}{}={}'.format(resultado3, sinal3, n3, (float(resultado3)*float(n3))))
    if sinal3 == '-':
        print('{}{}{}={}'.format(resultado3, sinal3, n3, (float(resultado3)-float(n3))))
    if sinal3 == '+':
        print('{}{}{}={}'.format(resultado3, sinal3, n3, (float(resultado3)+float(n3))))
