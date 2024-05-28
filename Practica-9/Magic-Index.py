#Solucion sencilla 
def indice_magico(A):

  izquierda = 0
  derecha = len(A) - 1
  while izquierda <= derecha:
    medio = (izquierda + derecha) // 2
    if A[medio] == medio:
      return medio
    elif A[medio] < medio:
      derecha = medio - 1
    else:
      izquierda = medio + 1
  return -1

# Aqui se modificara para meter el indece(Matriz) 
A = [-1, 0, 1, 2]
indice = indice_magico(A)
if indice != -1:
  print(f"Índice mágico: {indice}")
else:
  print("No hay índice mágico en la matriz")
