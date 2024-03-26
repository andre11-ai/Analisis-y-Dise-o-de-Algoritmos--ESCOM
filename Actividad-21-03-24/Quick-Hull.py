import matplotlib.pyplot as plt
import time
import random

# Función para encontrar el área signada de un triángulo formado por 3 puntos
def area_sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

# Función para encontrar los puntos más alejados de una línea
def find_hull_points(points, p1, p2, side, hull):
    max_dist = 0
    max_point = None
    for point in points:
        dist = area_sign(p1, p2, point)
        if dist * side > 0:
            if dist > max_dist:
                max_dist = dist
                max_point = point
    if max_point:
        hull.append(max_point)
        find_hull_points(points, p1, max_point, -area_sign(p1, max_point, p2), hull)
        find_hull_points(points, max_point, p2, -area_sign(max_point, p2, p1), hull)

# Algoritmo Quick Hull
def quick_hull(points):
    if len(points) < 3:
        return points

    # Encontrar los puntos extremos
    min_x = min(points, key=lambda p: p[0])
    max_x = max(points, key=lambda p: p[0])
    hull = [min_x, max_x]

    # Encontrar los puntos más alejados de la línea formada por los extremos
    find_hull_points(points, min_x, max_x, -1, hull)
    find_hull_points(points, max_x, min_x, -1, hull)

    return hull

# Generar n puntos aleatorios
n = 10
points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Calcular el tiempo de inicio
start_time = time.time()

# Calcular la envolvente convexa
convex_hull = quick_hull(points)

# Calcular el tiempo de fin
end_time = time.time()
elapsed_time = end_time - start_time
print("Tiempo de ejecución:", elapsed_time, "segundos")

# Visualizar los puntos y la envolvente convexa
x, y = zip(*points)
plt.plot(x, y, 'ro')
for i in range(1, len(convex_hull)):
    plt.plot([convex_hull[i-1][0], convex_hull[i][0]], [convex_hull[i-1][1], convex_hull[i][1]], 'b-')
plt.plot([convex_hull[-1][0], convex_hull[0][0]], [convex_hull[-1][1], convex_hull[0][1]], 'b-')
plt.show()