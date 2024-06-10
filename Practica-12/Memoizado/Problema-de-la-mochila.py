import time
import tracemalloc

# Función que resuelve el problema de la mochila utilizando memorización
def knapsack(wt, val, W, n, t):
    # Condiciones base
    if n == 0 or W == 0:
        return 0
    if t[n][W] != -1:
        return t[n][W]

    # Código del diagrama de elección
    if wt[n-1] <= W:
        t[n][W] = max(val[n-1] + knapsack(wt, val, W-wt[n-1], n-1, t),
                      knapsack(wt, val, W, n-1, t))
        return t[n][W]
    elif wt[n-1] > W:
        t[n][W] = knapsack(wt, val, W, n-1, t)
        return t[n][W]

# Código principal
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    
    # Inicializamos la matriz con -1 al principio
    t = [[-1 for i in range(W + 1)] for j in range(n + 1)]

    # Iniciar el seguimiento de memoria
    tracemalloc.start()

    # Iniciar el temporizador
    start_time = time.time()

    # Llamada a la función knapsack
    max_value = knapsack(weight, profit, W, n, t)

    # Parar el temporizador
    end_time = time.time()

    # Obtener el uso de memoria
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Valor máximo que se puede obtener: {max_value}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    print(f"Memoria usada actualmente: {current / 10**6} MB")
    print(f"Memoria máxima usada: {peak / 10**6} MB")
