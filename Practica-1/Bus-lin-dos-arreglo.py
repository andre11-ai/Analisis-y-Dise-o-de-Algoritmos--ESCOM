
import random
import time

inicio = time.time()

def busqueda_lineal(lista1, lista2, objetivo):
    for lista in [lista1, lista2]:
        if objetivo in lista:
            return True
    return False

if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista1 = [random.randint(0, 10000) for _ in range(tamano_de_lista)]
    lista2 = [random.randint(0, 10000) for _ in range(tamano_de_lista)]

    encontrado = busqueda_lineal(lista1, lista2, objetivo)
    print(lista1)
    print(lista2)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en ninguna de las listas')


fin = time.time()
print(fin-inicio)