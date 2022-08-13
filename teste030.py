p1 = str(input('Quer café? ')).lower().strip()
if p1 =='sim':
    p2 = str(input('Leite? ')).lower()
    p3 = str(input('Açucar? ')).lower()
    p4 = str(input('Adoçante? ')).lower()
    if p2 and p3 and p4 == 'sim':
        print('Café com Leite Açucar e Adoçante'.format(p2, p3, p4))
    if p2 and p3 == 'sim':
        print('Café com Leite Açucar')
    if p3 and p4 == 'sim':
        print('Café com Açucar e Adoçante')
    if p2 and p4 == 'sim':
        print('Café com Leite e Adoçante')
    if p2 == 'sim':
        print('Café com Leite')
    if p3 == 'sim':
        print('Café com Açucar')
    if p4 == 'sim':
        print('Café com Adoçante')
