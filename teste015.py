preco = float(input('Digite o preço do produto: R$'))
print('A vista com 10% de desconto: R${:.2f}'.format(preco-(preco*10/100)))
print('Parcelado no cartão com 7% de acrescimo R${:.2f}'.format(preco+(preco*7/100)))
