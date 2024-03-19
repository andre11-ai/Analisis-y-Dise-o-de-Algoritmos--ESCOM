import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Generar un arreglo de longitud n con números aleatorios
n = 10000000   #AQUI SE FUE MODIFICANDO LOS VALORES PARA DETERMINAR EL TIEMPO
arr = [random.randint(1, 100) for _ in range(n)]

print("Arreglo original:", arr)
start_time = time.time()  # Tiempo de inicio
sorted_arr = merge_sort(arr.copy())
end_time = time.time()  # Tiempo de finalización
print("Arreglo ordenado:", sorted_arr)
print("Tiempo de ejecución:", end_time - start_time, "segundos")