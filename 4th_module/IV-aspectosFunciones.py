"""
Las funciones tienen más cosas para decirnos. En este capítulo veremos otros detalles
como el significado de None como resultado de una función, el pasar argumentos a una
función y la instrucción return.

"""



# _______________________________________________________________________________



"""
La instrucción return tiene un comportamiento similar a continue y break.
Se usa para indicarle a una función cuál es el resultado que debe mostrar.

La presencia de None como resultado de una función se debe a la ausencia de la instrucción
return. Básicamente, return dice: el producto que genera esta función es...
"""



# Creamos una función que suma dos números
def suma(numero1, numero2):
       resultado = numero1 + numero2
       return resultado

print(suma(3, 5)) # Salida: 8. La función ya no arroja None como resultado.



# _______________________________________________________________________________



"""
La manera en la que le pasamos argumentos a una función puede afectar su funcionamiento.

- Argumentos posicionales:
  Asignan cada argumento al parámetro correspondiente, se ponen los argumentos
  en el orden de los parámetros. Es decir, si primero se crea numero1, el primer argumento en ponerse
  es el correspondiente a numero1.

- Paso de argumentos con palabras clave:
  En este caso, el argumento recibe el parámetro por su nombre.

  suma(3, numero2=5)


NOTAS:
- Si se desean combinar ambos pasos, primero se deben pasar los argumentos posicionales.

- Valor default de un parámetro:
  def suma(numero1, numero2=0)
  
  De la anterior forma se puede hacer que numero2 sea 0, pudíendose omitir a la hora de llamar
  la función.

"""