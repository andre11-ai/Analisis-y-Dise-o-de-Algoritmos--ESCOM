def mochila_fraccionaria(beneficios, pesos, capacidad):
  # Ordena los elementos por su relación beneficio-peso.
  elementos = sorted(zip(beneficios, pesos), key=lambda elemento: elemento[0] / elemento[1], reverse=True)

  # Inicializa la mochila con un conjunto vacío.
  mochila = []

  # Inicializa el beneficio total a 0.
  beneficio_total = 0

  # Recorre los elementos en orden de su relación beneficio-peso.
  for elemento in elementos:
    # Si el elemento cabe en la mochila, añádelo a la mochila.
    if elemento[1] <= capacidad:
      mochila.append(elemento)
      beneficio_total += elemento[0]
      capacidad -= elemento[1]
    # De lo contrario, añade una parte fraccionaria del elemento a la mochila.
    else:
      beneficio_fraccionario = elemento[0] / elemento[1] * capacidad
      beneficio_total += beneficio_fraccionario
      capacidad = 0
      break

  # Imprime el beneficio total.
  print("Beneficio total:", beneficio_total)

  # Devuelve los elementos en la mochila y el beneficio total.
  return mochila, beneficio_total


# Ejemplos de uso.
#Ejemplo 1
beneficios = [60, 100, 120]
pesos = [10, 20, 30]
capacidad = 50

#Ejemplo 2
#beneficios = [60, 100, 120, 180, 200]
#pesos = [10, 20, 30, 40, 50]
#capacidad = 80

#Ejemplo 3
#beneficios = [604, 100, 220]
#pesos = [148, 50, 80]
#capacidad = 200

mochila, beneficio_total = mochila_fraccionaria(beneficios, pesos, capacidad)

# Imprime los elementos en la mochila.
for elemento in mochila:
  print(elemento)