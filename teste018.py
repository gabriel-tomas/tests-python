print('Categorias:\nAnimais(Digite 1)\nComidas(Digite 2)\nObjetos(Digite 3)')
categoria = str(input('Qual categoria você deseja? '))
dificuldade = str(input('Escolha a dificuldade, sendo 1 = fácil, 2 = díficil '))
r_c_d = categoria+dificuldade
if r_c_d == '11':
 print('\nAnimal de 2 patas, com 4 letras: '), print('')
 while(1):
     l1 = str(input('______ '
                    '\n|'
                    '\n|'
                    '\n| ').title())
     if l1 == 'P':
        while(2):
            l2 = str(input('______ '
                           '\n|'
                           '\n|'
                           '\n| P').lower())
            if l2 =='a':
                while(3):
                   l3 = str(input('______ '
                                  '\n|'
                                  '\n|'
                                  '\n| P a').lower())
                   if l3=='t':
                        while(4):
                         l4 = str(input('______ '
                                        '\n|'
                                        '\n|'
                                        '\n| P a t').lower())
                         if l4 == 'o':
                            print('______ '
                                  '\n|'
                                  '\n|'
                                  '\n| P a t o')
                            quit()
if r_c_d == '21':
    print('Tem queijo e é redondo')
    while(1):
     a1 = input('Digite: ').title()
     if a1 =='P':
         while(2):
             a2 = input('P').lower()
             if a2 =='i':
                 while(3):
                     a3 = input('Pi')
                     if a3 =='z':
                         while(4):
                             a4 = input('Piz')
                             if a4 == 'z':
                                 while(5):
                                     a5 = input('Pizz')
                                     if a5 == 'a':
                                         print('Acertou Pizza')
                                         quit()
