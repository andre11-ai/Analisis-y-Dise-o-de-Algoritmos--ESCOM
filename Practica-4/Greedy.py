def cambio_optimo(V):
  
  # Inicializar el número de monedas a 0
  monedas = 0

  # Lista de monedas disponibles
  monedas_disponibles = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

  # Diccionario para almacenar el número de monedas de cada tipo
  monedas_usadas = {}

  # Iterar sobre las monedas disponibles en orden descendente
  for moneda in monedas_disponibles[::-1]:
    # Mientras el valor sea mayor o igual que la moneda actual
    while V >= moneda:
      # Restar la moneda del valor
      V -= moneda
      # Incrementar el número de monedas
      monedas += 1
      
      # Incrementar el número de monedas usadas de ese tipo
      if moneda not in monedas_usadas:
        monedas_usadas[moneda] = 0
      monedas_usadas[moneda] += 1

  # Devolver el número de monedas y el número de monedas usadas de cada tipo
  return monedas, monedas_usadas

# Valores de prueba
valores = [2550, 8432, 263]

# Calcular el número mínimo de monedas para cada valor
for valor in valores:
  monedas_minimas, monedas_usadas = cambio_optimo(valor)
  print(f"Para el valor {valor}, el número mínimo de monedas es {monedas_minimas}")
  print(f"Monedas usadas:")
  for moneda, cantidad in monedas_usadas.items():
    print(f"  {moneda}: {cantidad}")
