n = str(input('Faça um calculo: '))
a = n.split('+')
if n.count('+') == 1:
    print(int(a[0]) + int(a[1]))
else:
    while(1):
        m = str(input('Faça um calculo'))
        b = m.split('+')
        if m.count('+') == 1:
            print(int(b[0]) + int(b[1]))
