import random
import time

inicio = time.time()

def check_common_element(A, B):
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                return True
    return False

# Generar arrays de n números aleatorios
n = 10
A = [random.randint(1, 1000000) for _ in range(n)]
B = [random.randint(1, 1000000) for _ in range(n)]

# Verificar si hay elementos comunes
print("Array A:", A)
print("Array B:", B)
print("¿Hay elementos comunes?",check_common_element(A, B))

fin = time.time()
print(fin-inicio)