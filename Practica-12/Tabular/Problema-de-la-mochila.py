import time
import tracemalloc

# Función que resuelve el problema de la mochila
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Construcción de la tabla K[][] de manera ascendente
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

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
