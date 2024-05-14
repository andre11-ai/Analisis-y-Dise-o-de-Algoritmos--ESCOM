def subir_escalera(n, pasos_anteriores={}, camino=[], ultimo_paso=0):

    # Caso base:
    if n == 0:
        return 1, [camino]  # Se llegó al final de la escalera, una sola manera con el camino actual.
    elif n < 0:
        return 0, []  # No se puede subir una escalera negativa.

    # Revisar si la solución ya está memorizada:
    if n in pasos_anteriores and ultimo_paso in pasos_anteriores[n]:
        return pasos_anteriores[n][ultimo_paso]

    # Calcular las soluciones para cada paso posible, evitando repetir el mismo paso consecutivo:
    pasos_posibles = []
    for paso in [1, 2, 3]:
        if paso != ultimo_paso:
            total, caminos = subir_escalera(n - paso, pasos_anteriores, camino + [paso], paso)
            pasos_posibles.append((total, caminos))

    # Sumar las soluciones para cada paso posible:
    total_maneras = sum(total for total, _ in pasos_posibles)

    # Almacenar la solución para futuras llamadas:
    if n not in pasos_anteriores:
        pasos_anteriores[n] = {}
    pasos_anteriores[n][ultimo_paso] = total_maneras, [camino for _, caminos in pasos_posibles for camino in caminos]

    # Retornar el total de maneras de subir la escalera y todas las combinaciones de pasos:
    return total_maneras, [camino for _, caminos in pasos_posibles for camino in caminos]


# Solicitar al usuario ingresar el número de peldaños:
n = int(input("Ingrese el número de peldaños de la escalera: "))

# Calcular el número de maneras posibles de subir la escalera y todas las combinaciones de pasos:
total_maneras, todas_caminos = subir_escalera(n)

# Mostrar todas las combinaciones de pasos:
print("Todas las combinaciones de pasos:")
for i, camino in enumerate(todas_caminos, start=1):
    print(f"Combinación {i}: {camino}")

# Mostrar el total de maneras posibles:
print(f"\nNúmero total de maneras de subir una escalera de {n} peldaños:", total_maneras)
