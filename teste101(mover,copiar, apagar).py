import os
import shutil

caminho_raiz = r"C:\Users\Gabriel\Downloads\pasta1"
caminho_novo = r"C:\Users\Gabriel\Downloads\pasta_nova"

try:
    os.mkdir(caminho_novo)
except FileExistsError as error:
    print("\033[31mPasta", caminho_raiz, "já existe\033[m")

for raiz, diretorio, arquivos in os.walk(caminho_raiz):
    for i, arquivo in enumerate(arquivos):
        old_path_file = os.path.join(raiz, arquivo)
        new_path_file = os.path.join(caminho_novo, arquivo)
        shutil.copy(old_path_file, new_path_file)
        print(f"{i} arquivos movidos com sucesso")