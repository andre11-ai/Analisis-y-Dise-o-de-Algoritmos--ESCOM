def decodificar_texto(texto_codificado, arbol_huffman):
  
  #Decodifica el texto codificado utilizando el árbol de Huffman.
  #Devuelve el texto decodificado.
  
  texto_decodificado = ""
  nodo_actual = arbol_huffman

  for bit in texto_codificado:
    if bit == "0":
      nodo_actual = nodo_actual["izquierda"]
    else:
      nodo_actual = nodo_actual["derecha"]

    if nodo_actual["caracter"] is not None:
      texto_decodificado += nodo_actual["caracter"]
      nodo_actual = arbol_huffman

  return texto_decodificado


# Carga el texto codificado del archivo
with open("texto_codificado.txt", "r") as archivo:
  texto_codificado = archivo.read()

# Carga el árbol de Huffman del archivo
with open("arbol_huffman.txt", "r") as archivo:
  arbol_huffman = eval(archivo.read())

# Decodifica el texto codificado
texto_decodificado = decodificar_texto(texto_codificado, arbol_huffman)

# Guarda el texto decodificado en un archivo
with open("texto_decodificado.txt", "w") as archivo:
  archivo.write(texto_decodificado)

print("Descompresión completada. El texto decodificado se ha guardado en un archivo separado.")
