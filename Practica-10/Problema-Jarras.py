from collections import deque

def JarrasProblema():
    # Inicializamos la cola con el estado inicial (0, 0)
    queue = deque([(0, 0)])
    # Usamos un set para mantener un registro de los estados visitados
    visited = set((0, 0))

    # Mientras haya estados en la cola
    while queue:
        # Extraemos el estado actual
        state = queue.popleft()
        a, b = state

        # Si hemos alcanzado el objetivo (4 litros en la jarra de 5 litros)
        if a == 4:
            return state
        
        # Posibles movimientos
        moves = [
            (5, b),        # Llenar la jarra de 5 litros
            (a, 3),        # Llenar la jarra de 3 litros
            (0, b),        # Vaciar la jarra de 5 litros
            (a, 0),        # Vaciar la jarra de 3 litros
            (a - min(a, 3 - b), b + min(a, 3 - b)),  # Transferir de 5 a 3
            (a + min(b, 5 - a), b - min(b, 5 - a))   # Transferir de 3 a 5
        ]

        # Procesar los movimientos válidos y agregar a la cola si no han sido visitados
        for new_state in moves:
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

    return None

# Ejecutar la función y mostrar el resultado
result = JarrasProblema()
if result:
    print(f"Se encontró una solución: {result}")
else:
    print("No se encontró una solución.")
