import os

path = "C:/Users/Gabriel/Pictures/Screenshots"
find = "25"

quant_arquivos = 0
for raiz, diretorios, arquivos in os.walk(path):
    for arquivo in arquivos:
        if find in arquivo:
            try:
                quant_arquivos += 1
                caminho = os.path.join(raiz, arquivo)
                print(f"Caminho: \033[35m{caminho}\033[m")
                nome_arquivo, extensao = os.path.splitext(arquivo)
                print(f"Nome: \033[32m{nome_arquivo}\033[m\nExtensão: \033[33m{extensao}\033[m")
                tamanho = os.path.getsize(caminho)
                print(f"Tamanho: \033[34m{tamanho} B\033[m")
            except Exception as error:
                print("Erro desconhecido: {error}")

print(f"\n{quant_arquivos} arquivo(s) encontrado(s)")