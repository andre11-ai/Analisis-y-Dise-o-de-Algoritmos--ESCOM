# ALgoritmo Greedy Optimizado para este problema

def asignar_memoria(procesos, memoria):
  # Ordenar los procesos por tamaño no decreciente
  procesos.sort(key=lambda p: p[1], reverse=True)

  # Recorrer los procesos y asignarles memoria
  for proceso in procesos:
    for bloque in memoria:
      if bloque[1] >= proceso[1]:
        bloque[1] -= proceso[1]
        proceso.append(bloque[0])
        break
    else:
      # Asignar un nuevo bloque de memoria
      bloque_nuevo = [len(memoria) + 1, proceso[1]]
      memoria.append(bloque_nuevo)
      proceso.append(bloque_nuevo[0])

  # Ajustar los tamaños de los bloques de memoria
  for bloque in memoria:
    bloque[1] = max(bloque[1], bloque[0])

  # Calcular la memoria restante
  memoria_restante = 0
  for bloque in memoria:
    memoria_restante += bloque[1]

  return memoria_restante


procesos = [
  [1, 212],
  [2, 417],
  [3, 112],
  [4, 426],
]

memoria = [
  [1, 100],
  [2, 500],
  [3, 200],
  [4, 300],
  [5, 600],
]

memoria_restante = asignar_memoria(procesos, memoria)

print("Asignación de memoria:")
for proceso in procesos:
  print(f"Proceso {proceso[0]}: Bloque {proceso[2]}, Tamaño del proceso: {proceso[1]} KB")

print("\nAjuste de los tamaños de los bloques de memoria:")
for bloque in memoria:
  print(f"Bloque {bloque[0]}: Tamaño {bloque[1]} KB")

print(f"\nMemoria restante: {memoria_restante} KB")
