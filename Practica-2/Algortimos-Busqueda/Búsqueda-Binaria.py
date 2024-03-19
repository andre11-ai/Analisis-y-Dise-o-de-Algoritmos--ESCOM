import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


#Búsqueda binaria
#Elimina la mitad de las opciones en cada una de las rondas
# La lista debe estar ordenada en forma ascendente
def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    
    if limite_inferior is None:
       limite_inferior = 0 #Inicio de la lista
    if limite_superior is None:
       limite_superior = len(lista)-1 #Final de la lista
      
   #Si no hay intervalo, termina la funcion     
    if limite_superior < limite_inferior:
        return -1

 #--------------- Recursión ---------------
 # se busca el punto medio de la lista y se busca hacia abajo o hacia arriba, 
 # depende el objetivo (si es mayor o menor que el punto medio)
 
    punto_medio = (limite_inferior + limite_superior) // 2 #usamos division entera (trunca los decimales)
    
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)




if __name__=='__main__':

    #Crear una lista ordenada con 10000 numeros aleatorios.
    tamaño = 10000000    #AQUI SE FUE MODIFICANDO LOS VALORES PARA DETERMINAR EL TIEMPO
    
    conjunto_inicial = set() #creamos un conjunto (no se repiten los valores que contiene)
    
    #Lo llenamos con un while
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
        
    #convertimos "conjunto_inicial" en lista y la ordenamos con "sorted"
    lista_ordenada = sorted(list(conjunto_inicial))
    
    #Medir el tiempo con busqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")
       
    
    #Medir el tiempo de busqueda binaria
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")
    
    