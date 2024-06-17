import random

# Definir el sistema de ecuaciones
def equations(x, y, z, t):
    eq1 = x + 2*y - z + 3*t + 8
    eq2 = 2*x + 2*z - t - 13
    eq3 = -x + y + z - t - 8
    eq4 = 3*x + 3*y - z + 2*t + 1
    return eq1, eq2, eq3, eq4

# Inicializar variables
iterations = 10_000_000
best_solution = None
best_error = float('inf')

# Función para calcular el error total
def total_error(eq1, eq2, eq3, eq4):
    return abs(eq1) + abs(eq2) + abs(eq3) + abs(eq4)

# Realizar las iteraciones
for _ in range(iterations):
    x = random.randint(-5, 5)
    y = random.randint(-5, 5)
    z = random.randint(-5, 5)
    t = random.randint(-5, 5)

    eq1, eq2, eq3, eq4 = equations(x, y, z, t)
    error = total_error(eq1, eq2, eq3, eq4)

    if error == 0:
        best_solution = (x, y, z, t)
        best_error = error
        break
    elif error < best_error:
        best_solution = (x, y, z, t)
        best_error = error

# Imprimir la solución más cercana encontrada
if best_solution:
    print("Solución más cercana:", best_solution)
    print("Error asociado:", best_error)
else:
    print("No se encontró una solución exacta.")
