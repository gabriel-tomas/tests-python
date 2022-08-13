from time import sleep
from random import randint
n = int(input())
cor = 1
corrandom = 6
espaco = ''
num = 88
for nums in range(0, n+1):
    print(f'\r\033[4{cor-1};3{cor}m{espaco}',nums, end='\033[m')
    cor += 1
    if cor == corrandom:
        cor = cor - cor
        corrandom = randint(1, 6)
    sleep(0.010)
