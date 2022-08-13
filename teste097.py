if __name__ == "__main__":  
    from math import ceil

def mult_2(num):
    return num * 2

def two_list(list):
    middle = ceil((len(list) / 2))
    list1 = list[:middle]
    list2 = list[middle:]
    return list1, list2

def join_lists(*args):
    list_main = []
    for lists in args:
        list_main.extend(lists)
    return list_main

if __name__ == "__main__":
    lista = [2, 3, 4, 5, 6, 7, 2]
    lista2 = [1, 2, 3, 4, 5, 6, 7]
    list3 = [2, 3, 4, 534, 54, 45]
    list1 = join_lists(lista, lista2, list3)
    print(list1)
