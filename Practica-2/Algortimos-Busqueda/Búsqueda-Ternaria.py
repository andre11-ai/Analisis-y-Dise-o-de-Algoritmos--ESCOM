import random
import time

# Función de búsqueda ternaria
def busqueda_ternaria(arreglo, llave):
    izquierda, derecha = 0, len(arreglo) - 1
    while izquierda <= derecha:
        tercio_1 = izquierda + (derecha - izquierda) // 3
        tercio_2 = derecha - (derecha - izquierda) // 3
        if arreglo[tercio_1] == llave:
            return tercio_1
        elif arreglo[tercio_2] == llave:
            return tercio_2
        elif arreglo[tercio_1] > llave:
            derecha = tercio_1 - 1
        elif arreglo[tercio_2] < llave:
            izquierda = tercio_2 + 1
        else:
            izquierda = tercio_1 + 1
            derecha = tercio_2 - 1
    return -1

# Generar arreglo de números aleatorios
n = 10000000        #AQUI SE FUE MODIFICANDO LOS VALORES PARA DETERMINAR EL TIEMPO
arreglo = [random.randint(1, 100) for _ in range(n)]
llave = random.choice(arreglo)

# Realizar la búsqueda ternaria
start_time = time.time()  # Tiempo de inicio
indice = busqueda_ternaria(arreglo, llave)
end_time = time.time()  # Tiempo de finalización

# Imprimir resultados y tiempo de ejecución
if indice != -1:
    print(f'El elemento {llave} se encontró en el lugar {indice + 1} del arreglo {arreglo}.')
else:
    print(f'El elemento {llave} no se encontró en el arreglo {arreglo}.')
print("Tiempo de ejecución:", end_time - start_time, "segundos")