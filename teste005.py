nome = input('Bem vindo ao shopping, diga seu nome: ')
escolha = input('O que você deseja {}? '.format(nome))
help='ajuda'
if escolha == help:
    ajuda=input('{}, que tipo de ajuda?'.format(nome))
    if ajuda == 'número da empresa':
       print('81 92323-3382')
    if ajuda == 'certificado da empresa':
       print('entre no site http//:www.google.com.br')
if escolha == 'rastreamento':
 print('clique no canto superior da tela, lá esta o lugar de rastreamento de objetos')









