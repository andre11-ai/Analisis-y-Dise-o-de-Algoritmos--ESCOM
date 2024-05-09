from collections import deque

def capturar_texto():
  
  #Captura un texto del usuario y lo devuelve como cadena.
  
  texto = input("Ingrese el texto que desea comprimir: ")
  return texto

def analizar_frecuencias(texto):
  
  #Analiza la frecuencia de ocurrencia de cada caracter en el texto.
  #Devuelve un diccionario con las frecuencias.
  
  frecuencias = {}
  for caracter in texto:
    if caracter in frecuencias:
      frecuencias[caracter] += 1
    else:
      frecuencias[caracter] = 1
  return frecuencias

# Captura el texto del usuario
texto_original = capturar_texto()

# Analiza las frecuencias de cada caracter
frecuencias = analizar_frecuencias(texto_original)

# Imprime las frecuencias de cada caracter
print("Frecuencias de caracteres:")
for caracter, frecuencia in frecuencias.items():
  print(f"{caracter}: {frecuencia}")


def crear_nodo(caracter, frecuencia):
  
  #Crea un nodo del árbol de Huffman.
  
  return {"caracter": caracter, "frecuencia": frecuencia, "izquierda": None, "derecha": None}

def construir_arbol_huffman(frecuencias):
  
  #Construye el árbol de Huffman a partir de las frecuencias de los caracteres.
  
  cola_prioridad = deque()
  for caracter, frecuencia in frecuencias.items():
    nodo = crear_nodo(caracter, frecuencia)
    cola_prioridad.append(nodo)

  while len(cola_prioridad) > 1:
    nodo_izquierdo = cola_prioridad.popleft()
    nodo_derecho = cola_prioridad.popleft()

    nodo_padre = crear_nodo(None, nodo_izquierdo["frecuencia"] + nodo_derecho["frecuencia"])
    nodo_padre["izquierda"] = nodo_izquierdo
    nodo_padre["derecha"] = nodo_derecho

    cola_prioridad.append(nodo_padre)

  return cola_prioridad.pop()

def codificar_caracter(nodo, codigo, codigos):
  
  #Recorre el árbol de Huffman y asigna códigos binarios a cada caracter.
  
  if nodo["caracter"] is not None:
    codigos[nodo["caracter"]] = codigo
  else:
    codificar_caracter(nodo["izquierda"], codigo + "0", codigos)
    codificar_caracter(nodo["derecha"], codigo + "1", codigos)

def codificar_texto(texto, codigos):

  #Codifica el texto original utilizando los códigos de Huffman.
  #Devuelve el texto codificado como cadena binaria.
  
  texto_codificado = ""
  for caracter in texto:
    texto_codificado += codigos[caracter]
  return texto_codificado

# Construye el árbol de Huffman
arbol_huffman = construir_arbol_huffman(frecuencias)

# Crea un diccionario con los códigos de Huffman para cada caracter
codigos = {}
codificar_caracter(arbol_huffman, "", codigos)

# Codifica el texto original
texto_codificado = codificar_texto(texto_original, codigos)

def guardar_texto(nombre_archivo, texto):
  """
  Guarda el texto en un archivo.
  """
  with open(nombre_archivo, "w") as archivo:
    archivo.write(texto)

# Guarda el texto original en un archivo
guardar_texto("texto_original.txt", texto_original)

# Guarda el texto codificado en un archivo
guardar_texto("texto_codificado.txt", texto_codificado)

print("Compresión completada. El texto original y codificado se han guardado en archivos separados.")

def guardar_arbol_huffman(nombre_archivo, arbol_huffman):
  with open(nombre_archivo, "w") as archivo:
    archivo.write(str(arbol_huffman))

# Construye el árbol de Huffman
arbol_huffman = construir_arbol_huffman(frecuencias)

# Guarda el árbol de Huffman en un archivo
guardar_arbol_huffman("arbol_huffman.txt", arbol_huffman)

