import time
import tracemalloc

# Función recursiva para contar el número de formas de sumar
# monedas[0...n-1] para obtener la suma "sum"
def count(coins, n, sum):
    # Si la suma es 0, entonces hay 1 solución (no incluir ninguna moneda)
    if sum == 0:
        return 1

    # Si la suma es menor que 0, entonces no existe solución
    if sum < 0:
        return 0

    # Si no hay monedas y la suma es mayor que 0, entonces no existe solución
    if n <= 0:
        return 0

    # El recuento es la suma de soluciones (i) incluyendo coins[n-1] (ii) excluyendo coins[n-1]
    return count(coins, n - 1, sum) + count(coins, n, sum - coins[n-1])

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
