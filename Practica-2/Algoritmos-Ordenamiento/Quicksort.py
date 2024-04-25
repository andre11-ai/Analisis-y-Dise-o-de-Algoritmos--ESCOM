import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


# Generar un arreglo de longitud n con números aleatorios
n = 10000     #AQUI SE FUE MODIFICANDO LOS VALORES PARA DETERMINAR EL TIEMPO
arr = [random.randint(1, 100) for _ in range(n)]

print("Arreglo original:", arr)
start_time = time.time()  # Tiempo de inicio
sorted_arr = quick_sort(arr.copy())
end_time = time.time()  # Tiempo de finalización
print("Arreglo ordenado:", sorted_arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")