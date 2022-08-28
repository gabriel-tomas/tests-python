list = [2]
if list:
    print("A lista esta com itens")
else:
    print("A lista esta \033[1mvazia\033[m")
list.clear()
if list:
    print("A lista \033[1mainda\033[m esta com itens")
else:
    print("A lista foi limpada")