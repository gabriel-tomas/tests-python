file = open('Texto.txt', 'w+')
file.write('123')
file.seek(0, 0)
print(file.read())
