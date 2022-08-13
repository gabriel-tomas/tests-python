preco = float(input('Digite o preço: R$'))
cartao_ou_avista = input('Cartão ou Avista (Digite 1 para cartão ou 2 para Avista): ')
acrescimo_cartao = preco+preco*4/100
if cartao_ou_avista == '1':
 print('No cartão há um acrescimo de 4%, antes o preco era {}, agora é {:.2f}'.format(preco, acrescimo_cartao))
if cartao_ou_avista == '2':
    desconto = int(input('Digite o desconto: '))
    pf = preco-preco*desconto/100
    print('O preço era {:.2f}R$ e com o desconto de {}% ficou por {:.2f}R$'.format(preco, desconto, pf))
