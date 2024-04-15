# ALgoritmo Greedy Original para este problema

# Crea una lista de procesos y sus tamaños 
procesos = [
    {"id": 1, "tamaño": 212},
    {"id": 2, "tamaño": 417},
    {"id": 3, "tamaño": 112},
    {"id": 4, "tamaño": 426},
]

# Crea una lista de bloques de memoria y sus tamaños
bloques = [
    {"id": 1, "tamaño": 100},
    {"id": 2, "tamaño": 500},
    {"id": 3, "tamaño": 200},
    {"id": 4, "tamaño": 300},
    {"id": 5, "tamaño": 600},
]

# Función para asignar un bloque de memoria a un proceso
def asignar_bloque(proceso, bloque):
    # Actualiza el tamaño del bloque
    bloque["tamaño"] -= proceso["tamaño"]
    
    # Asigna el bloque al proceso
    proceso["bloque"] = bloque

# Recorre los procesos
for proceso in procesos:
    # Busca un bloque de memoria disponible
    for bloque in bloques:
        # Verifica si el bloque tiene suficiente espacio para el proceso
        if bloque["tamaño"] >= proceso["tamaño"]:
            # Asigna el bloque al proceso
            asignar_bloque(proceso, bloque)
            break
    
    # Imprime el estado del proceso y el tamaño del proceso
    if "bloque" in proceso:
        print(f"Proceso {proceso['id']} asignado al bloque {proceso['bloque']['id']} (Tamaño del proceso: {proceso['tamaño']} KB)")
    else:
        print(f"Proceso {proceso['id']} no asignado")

# Ajusta los tamaños de los bloques de memoria
for bloque in bloques:
    # Si el tamaño del bloque es menor que el tamaño mínimo, ajusta el tamaño al tamaño mínimo
    if bloque["tamaño"] < 100:
        bloque["tamaño"] = 100

# Imprime los tamaños ajustados de los bloques de memoria
print("\nAjuste de los tamaños de los bloques de memoria:")
for bloque in bloques:
    print(f"Bloque {bloque['id']}: {bloque['tamaño']} KB")

# Calcula la memoria restante
memoria_restante = 0
for bloque in bloques:
    memoria_restante += bloque["tamaño"]

print(f"\nMemoria restante: {memoria_restante} KB")
