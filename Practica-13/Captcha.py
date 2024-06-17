import random
import matplotlib.pyplot as plt

# Función para escribir los puntos en un archivo
def guardar_puntos_en_archivo(puntos, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        for punto in puntos:
            archivo.write(f"{punto[0]},{punto[1]}\n")

# Generar las coordenadas de un triángulo equilátero
def generar_triangulo_equilatero():
    V1 = (0, 0)
    V2 = (1, 0)
    V3 = (0.5, (3 ** 0.5) / 2)
    return V1, V2, V3

# Generar los puntos siguiendo el algoritmo
def generar_puntos(triangulo, punto_inicial, iteraciones):
    V1, V2, V3 = triangulo
    P = punto_inicial
    puntos = [P]

    for _ in range(iteraciones):
        vertice = random.choice([V1, V2, V3])
        P = ((P[0] + vertice[0]) / 2, (P[1] + vertice[1]) / 2)
        puntos.append(P)
    
    return puntos

# Graficar los puntos
def graficar_puntos(puntos):
    x_coords = [punto[0] for punto in puntos]
    y_coords = [punto[1] for punto in puntos]
    plt.scatter(x_coords, y_coords, s=0.1)  # s es el tamaño del punto
    plt.show()

# Parámetros
punto_inicial = (random.uniform(0, 1), random.uniform(0, (3 ** 0.5) / 2))
iteraciones = 1000000
nombre_archivo = 'puntos_sierpinski.txt'

# Generar triángulo equilátero
triangulo = generar_triangulo_equilatero()

# Generar puntos
puntos = generar_puntos(triangulo, punto_inicial, iteraciones)

# Guardar puntos en un archivo
guardar_puntos_en_archivo(puntos, nombre_archivo)

# Graficar puntos
graficar_puntos(puntos)
