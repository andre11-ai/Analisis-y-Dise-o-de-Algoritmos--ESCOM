import random
import time

inicio = time.time()

def check_duplicates(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                return True
    return False

# Generar un array de n números aleatorios
n = 1000000
array = [random.randint(1, 1000000) for _ in range(n)]

# Verificar si hay duplicados
print("Array:", array)
print("¿Contiene duplicados?", check_duplicates(array))

fin = time.time()
print(fin-inicio)