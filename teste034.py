import datetime
p1 = str(input('Digite algo para aparecer a data atual\n'))
if p1.isalpha():
    print('\nHoje é', datetime.date.today())
p2 = str(input('\nDigite algo para aparecer a hora atual\nou apenas enter para sair '))
if p2.isalpha():
    aspt = datetime.datetime.now()
    aspt1 = str(aspt).split()
    print('\nA Hora é', aspt1[1][0:5])
