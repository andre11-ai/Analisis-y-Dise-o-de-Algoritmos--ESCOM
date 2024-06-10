import time
import tracemalloc

# Función recursiva para contar el número de formas distintas de hacer la suma usando n monedas
def count(coins, sum, n, dp):
    # Caso base
    if sum == 0:
        dp[n][sum] = 1
        return dp[n][sum]

    # Si el número de monedas es 0 o la suma es menor que 0, entonces no hay forma de hacer la suma.
    if n == 0 or sum < 0:
        return 0

    # Si el subproblema se ha calculado previamente, simplemente devuelve el resultado
    if dp[n][sum] != -1:
        return dp[n][sum]

    # Dos opciones para la moneda actual
    dp[n][sum] = count(coins, sum - coins[n - 1], n, dp) + count(coins, sum, n - 1, dp)

    return dp[n][sum]

# Código principal
if __name__ == '__main__':
    n = 3
    sum = 5
    coins = [1, 2, 3]
    dp = [[-1 for i in range(sum + 1)] for j in range(n + 1)]
    
    # Iniciar el seguimiento de memoria
    tracemalloc.start()

    # Iniciar el temporizador
    start_time = time.time()

    # Llamada a la función count
    res = count(coins, sum, n, dp)

    # Parar el temporizador
    end_time = time.time()

    # Obtener el uso de memoria
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"El número de formas distintas de hacer la suma {sum} es: {res}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
    print(f"Memoria usada actualmente: {current / 10**6} MB")
    print(f"Memoria máxima usada: {peak / 10**6} MB")
