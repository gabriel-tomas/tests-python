try:
    b = int(input(":"))
except NameError as erro:
    b = 0
    print("Ocorreu um erro:", erro)
except Exception as erro:
    b = 0
    print("Ocorreu um erro inesperado", erro)
else:
    print("O codigo foi um rodado com sucesso")
finally:  
    print("Bloco de tratamento de erro terminado")
print(b)