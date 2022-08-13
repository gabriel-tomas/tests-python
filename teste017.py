largura = float(input('Digite a largura da parede(m): '))
altura = float(input('Digite a altura da parede(m): '))
area = largura*altura
litro_por_metro_quadrado = float(input('Digite quantos m² ela pinta por litro: '))
p = area/litro_por_metro_quadrado
print('Área da parede é {:.2f}m²'.format(area))
print('Você vai precisar de {:.1f}L Litros de tinta para pintar sua parede'.format(p))
