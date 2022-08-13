from datetime import date
from time import sleep

a = 23
b = 2

print(f'o valor de a é {a} e b é {b}')
c = int(input('Digite C: '))
print(f'o valor de c multiplicado por b é: {c * b}\n')


print('Quantos anos você tem? ')
resp = int(input('Digite: '))
if 18 <= resp <= 30:
    print(f'Você é maior de idade e nasceu em {date.today().year - resp}')
elif resp < 18:
    print(f'Você é menor de idade e nasceu em {date.today().year - resp}')
else:
    print(f'Você é velho e naceu em {date.today().year - resp}')
print()


for c in range(1, 4):
    print(f'\rAguarde {c}s', end='')
    sleep(1)
print()
vezes = 0
while True:
    conti = str(input('\nDigite N para parar: '))
    if conti == 'Nn':
        break
    else:
        vezes += 1
        print(f'Você continuou {vezes}')
print()


num = int(input('Digite um valor: '))
def dividir_2(valor):
    resultado = valor / 2
    print(resultado)
dividir_2(num)
print()

tupla = (4, 2, 'y')
print(f'A tupla é {tupla} e o valor 0 dela é {tupla[0]}')
list = [2, 3, 5]
print(f'A lista é {list} e o valor 1 dela é {list[1]}')
dic = {'valor0': 23, 'valor1': 2, 'valor2': 5}
print(f'O dicionário é {dic} e o valor da chave 2 é {dic["valor3"]}')
