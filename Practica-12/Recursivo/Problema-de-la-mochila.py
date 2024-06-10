import time
import tracemalloc

# Función recursiva que resuelve el problema de la mochila
def knapSack(W, wt, val, n):

    # Caso base
    if n == 0 or W == 0:
        return 0

    # Si el peso del enésimo objeto es mayor que la capacidad W de la mochila,
    # entonces este objeto no puede ser incluido en la solución óptima
    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)

    # Devuelve el máximo de dos casos:
    # (1) el enésimo objeto es incluido
    # (2) no se incluye
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))

# Código principal
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)

    # Iniciar el seguimiento de memoria
    tracemalloc.start()

    # Iniciar el temporizador
    start_time = time.time()

    # Llamada a la función knapSack
    max_value = knapSack(W, weight, profit, n)

    # Parar el temporizador
    end_time = time.time()

    # Obtener el uso de memoria
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Valor máximo que se puede obtener: {max_value}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    print(f"Memoria usada actualmente: {current / 10**6} MB")
    print(f"Memoria máxima usada: {peak / 10**6} MB")
