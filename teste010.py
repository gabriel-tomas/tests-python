print('Quer saber as regras?')
R=input('')
s=str('sim')
print()
if R == s:
 print('Regras:')
 print('Divisão= /')
 print('Soma= +')
 print('Subtração= -')
 print('Multiplicação= x')
 print('Potência= ^')
print()
n1 = float(input('Digite primeiro número: '))
sinal = input('({}) Digite o sinal de operação:'.format(n1))
n2 = float(input('({}{}) Digite o segundo número: '.format(n1, sinal)))
if sinal == '+':
 print('({}{}{}'.format(n1, sinal, n2)+'= {})'.format(n1+n2))
if sinal == '-':
 print('({}{}{}'.format(n1, sinal, n2)+'= {})'.format(n1-n2))
if sinal == '/':
 print('({}{}{}'.format(n1, sinal, n2)+'= {})'.format(n1/n2))
 sobra=input('Você quer o resultado da sobra da divisão?')
 if sobra == 'sim':
  print('sobrou {}'.format(n1%n2))
if sinal == 'x':
    print('({}{}{}'.format(n1, sinal, n2)+'= {})'.format(n1*n2))
if sinal == '^':
    print('({}{}{}'.format(n1,sinal,n2)+'={})'.format(n1**n2))