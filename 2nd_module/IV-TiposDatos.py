"""
Los datos son pieza fundamental en la programación.

Por ahora, distingiremos entre datos numéricos, de cadena y lógicos


NUMÉRICOS:
  - int: Número entero, como 1, 54, -23, 24624362
  - float: decimal. Se llama float por el punto 'flotante'. Ej 3.1516


CADENAS:
- texto: Cualquier caracter que esté entre comillas es una cadena.
  Ejemplo: 'Soy una cadena', "yo también lo soy", '576'.


LÓGICO:
- Booleano: Un tipo de dato booleano (abreviado como bool) es aquel que
  representa dos valores. Falso o Verdadero.
  Ejemplo: ¿Eres wuapo/a? True. ¿Eres débil? False.

"""



"""
NOTAS:
- Solo se puede sumar int + int y float + float. Intentar int + float es un error
- Se puede sumar un número y una variable, siempre y cuando ambas entidades
  sean números...
  ...se aplica la primera nota.
  
"""



# ________________________________________________________________

# Veámos lo aprendido

numeroDos = 2

suma = 5 + numeroDos # Se puede sumar un número y una variable, siempre y cuando ambos sean números

resta = numeroDos - 1

variable1 = 6.12 + 45 # Error, porque se suma float + int

saludo = 'Hello'

verdadero = True

falso = False

pi = 3.1416



# ________________________________________________________________


"""
EXPERIMENTA:

¿Qué pasa si sumas una cadena con un int?

¿Qué pasa si pones una variable dentro de un print()? -> print(variable)
"""