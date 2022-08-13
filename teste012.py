nome = str(input('Diga seu nome: '))
print('Bem vindo {}!'.format(nome))
idade = int(input('{} Diga sua idade: '.format(nome)))
mes = str(input('{} Diga o mês que você nasceu: '.format(nome)))
dia = input('{} Diga o dia que você nasceu: '.format(nome))
ano = int(input('{} Diga o ano atual: '.format(nome)))
print('{}, a data que vc nasceu foi {} do {} de {}'.format(nome, dia, mes, (ano-idade)))
ano_que_nasceu = ano-idade
if ano_que_nasceu >= 2004:
    print('Muito novo')
if ano_que_nasceu <= 2003:
    print('Muito velho')
