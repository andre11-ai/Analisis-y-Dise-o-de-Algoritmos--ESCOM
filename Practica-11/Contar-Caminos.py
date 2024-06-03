def contar_caminos(matriz, m, n):

  # Se crea una matriz para almacenar el número de rutas para cada casilla.
  dp = [[0 for _ in range(n)] for _ in range(m)]

  # Se inicializa la casilla inicial con 1 (una ruta posible).
  dp[0][0] = 1

  # Se recorre la matriz fila por fila y columna por columna.
  for i in range(m):
    for j in range(n):
      # Si la casilla actual es un obstáculo, se ignora.
      if matriz[i][j] == 1:
        continue

      # Se calculan las rutas posibles para la casilla actual sumando las rutas de las casillas adyacentes.
      if i > 0:
        dp[i][j] += dp[i - 1][j]
      if j > 0:
        dp[i][j] += dp[i][j - 1]

  # Se retorna el número de rutas en la casilla final (m, n).
  return dp[m - 1][n - 1]

# Ejemplos de uso

matriz = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]

#matriz = [
# [0, 0, 0, 1],
# [0, 1, 0, 0],
# [0, 0, 0, 0],
# [0, 0, 0, 0]
#]

#matriz = [
#  [0, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 1, 0, 0],
#  [1, 0, 0, 0]
#]

m = len(matriz)
n = len(matriz[0])

numero_caminos = contar_caminos(matriz, m, n)
print(f"El número de rutas posibles en el laberinto es: {numero_caminos}")
