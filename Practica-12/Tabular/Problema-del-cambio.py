import time
import tracemalloc

# Implementación del problema de cambio de monedas usando programación dinámica
def count(coins, n, sum):
    # dp[i] almacenará el número de soluciones para el valor i.
    # Necesitamos sum+1 filas ya que dp se construye de manera ascendente usando el caso base (sum = 0)
    # Inicializar todos los valores de la tabla como 0
    dp = [0 for k in range(sum + 1)]

    # Caso base (si el valor dado es 0)
    dp[0] = 1

    # Escoger todas las monedas una por una y actualizar los valores dp[]
    # después del índice mayor o igual al valor de la moneda escogida
    for i in range(0, n):
        for j in range(coins[i], sum + 1):
            dp[j] += dp[j - coins[i]]

    return dp[sum]

# Código principal para probar la función anterior
if __name__ == '__main__':
    coins = [1, 2, 3]
    n = len(coins)
    target_sum = 5

    # Iniciar el seguimiento de memoria
    tracemalloc.start()

    # Iniciar el temporizador
    start_time = time.time()

    # Llamada a la función count
    result = count(coins, n, target_sum)

    # Parar el temporizador
    end_time = time.time()

    # Obtener el uso de memoria
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"El número de formas de obtener la suma {target_sum} es: {result}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    print(f"Memoria usada actualmente: {current / 10**6} MB")
    print(f"Memoria máxima usada: {peak / 10**6} MB")
