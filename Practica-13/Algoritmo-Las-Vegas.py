import random

def punto_aleatorio_circulo():
    while True:
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            return x, y

# Ejemplo de uso
punto = punto_aleatorio_circulo()
print("Punto aleatorio dentro del círculo unitario:", punto)
