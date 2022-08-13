lista = input('Quais itens foram vendidos?')
resultado_do_numero_de_itens=len(lista)
quantidade_dos_itens=input('vc quer saber quantos itens foram vendidos?')
if quantidade_dos_itens=='sim':
 print('total de itens da lista é {}'.format(resultado_do_numero_de_itens))
if resultado_do_numero_de_itens>=24:
    print('promoção de 5%')
if resultado_do_numero_de_itens<=10:
    print('promoção de 2%')
