import math

def SquareRootBinarySearch(num):
    # Si el número es 0 o 1, su raíz cuadrada es el mismo número.
    if num == 0 or num == 1:
        return num

    # Inicializamos los límites izquierdo y derecho de la búsqueda (Busqueda binaria).
    l = 1
    r = num

    # Inicializamos la respuesta a 0.
    ans = 0

    # Mientras el límite izquierdo sea menor o igual que el límite derecho,
    # continuamos la búsqueda.
    while l <= r:
        # Calculamos el punto medio entre los límites.
        mid = l + (r - l) // 2

        # Comprobamos si el punto medio es la raíz cuadrada del número.
        if mid == num // mid:
            # Si lo es, devolvemos el punto medio como la respuesta.
            return mid
        elif mid < num // mid:
            # Si el punto medio es menor que la raíz cuadrada, actualizamos la respuesta al
            # punto medio y movemos el límite izquierdo al punto medio más 1.
            ans = mid
            l = mid + 1
        else:
            # Si el punto medio es mayor que la raíz cuadrada, movemos el límite derecho al
            # punto medio menos 1.
            r = mid - 1

    # Si no encontramos la raíz cuadrada exacta, devolvemos la respuesta
    # aproximada.
    return ans

# Solicitamos al usuario que ingrese un número para calcular su raíz cuadrada.
num = int(input("Ingrese un número que desea calcular la raíz cuadrada de: "))

# Llamamos a la función `SquareRootBinarySearch` para calcular la raíz cuadrada del número
# ingresado.
ans = SquareRootBinarySearch(num)

# Imprimimos el resultado en la consola.
print("La raíz cuadrada es:", ans)
