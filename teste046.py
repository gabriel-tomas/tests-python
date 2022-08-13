mediaidade = mediaaltura = menorq18 = c = 0
while True:
    p = str(input('Digite ENTER para mais uma pessoa ou "0" para sair: ')).strip()
    if p == '0':
        break
    i = int(input('Digite sua idade: '))
    a = float(input('Digite sua altura: '))
    mediaidade += i
    mediaaltura += a
    c += 1
    if i < 18:
        menorq18 += 1
print(f'{c}<<< total de pessoas\n'
      f'{mediaaltura/c:.2f}<<< media da altura\n'
      f'{mediaidade/c}<<< media da idade\n'
      f'{menorq18}<<< pessoas com menos de 18')
