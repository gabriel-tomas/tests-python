print('\033[32m=-'*12, '\033[32mCalculadora\033[m', '\033[32m-=' * 12)
soma = 0
for ca in range(0, 4):
    a = str(input(''))
    if a[0] == '+':
        b = a.split('+')
        soma = soma + float(b[1])
        print(soma, end='')
    elif a[1] or a[2] or a[3] or a[4] or a[5] or a[6] or a[7] or a[8] or a[9] == '+':
        spt = str(a).split('+')
        soma = soma + float(spt[0]) + float(spt[1])
        print(soma, end='')

