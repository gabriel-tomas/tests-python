numero1=int(input('Primeiro número: '))
numero2=int(input('Segundo número: '))
operacao=input('Qual operação você quer para esses números?')
if operacao=='+':
 print('O resultado da soma é:',numero1+numero2)
if operacao=='-':
 print('O resultado da subtração é:',numero1-numero2)
if operacao=='/':
 print('O resultado da divisão é:',numero1/numero2)
if operacao=='x':
 print('O resultado da multiplicação é:',numero1*numero2)
if operacao=='^':
 print('O resultado da potenciação é:',numero1**numero2)
if operacao=='resto da divisão':
 print('O resto de sua divisão é:',numero1%numero2)

sair=input('Sair do programa?')
if sair=='sim':
   quit('até mais')
if sair=='não':
   numero1 = int(input('Primeiro número: '))
   numero2 = int(input('Segundo número: '))
   operacao = input('Qual operação você quer para esses números?')
   if operacao == '+':
      print('O resultado da soma é:', numero1 + numero2)
   if operacao == '-':
      print('O resultado da subtração é:', numero1 - numero2)
   if operacao == '/':
      print('O resultado da divisão é:', numero1 / numero2)
   if operacao == 'x':
      print('O resultado da multiplicação é:', numero1 * numero2)
   if operacao == '^':
      print('O resultado da potenciação é:', numero1 ** numero2)
   if operacao == 'resto da divisão':
      print('O resto de sua divisão é:', numero1 % numero2)
