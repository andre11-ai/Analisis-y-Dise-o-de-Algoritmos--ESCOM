import random

def aproximar_pi(numero_de_puntos):
    puntos_dentro_del_circulo = 0
    
    for _ in range(numero_de_puntos):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            puntos_dentro_del_circulo += 1
    
    return (puntos_dentro_del_circulo / numero_de_puntos) * 4

# Ejemplo de uso
numero_de_puntos = 1000000  # Puedes ajustar este número para mayor precisión
pi_estimado = aproximar_pi(numero_de_puntos)
print("Estimación de Pi:", pi_estimado)
