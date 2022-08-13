c = contmais = contmenos = cmenos = 0
sinal = ''
while True:
    print('=' * 25)
    a = int(input('Digite o valor: '))
    b = int(input('Digite outro valor: '))
    print('=' * 25)
    print('''[ 1 ] Somar
[ 2 ] Subtrair
[ 3 ] Multiplicar
[ 4 ] Dividir
[ 5 ] Raiz
[ 6 ] Potenciação''')
    oper = int(input('Opção: '))
    print(f'{"Soma":-^25}')
    if oper == 1:
        soma = a + b
        print(soma)
        continuar = ' '
        while True:
            continuar = str(input('Continuar a soma [S/N]?')).upper()[0]
            if continuar == 'N':
                break
            c = int(input('Digite valor: '))
            if c == 0:
                soma -= soma
            soma += c
            print(soma)
        print(f'{"Final":-^25}')


