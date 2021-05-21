"""
Ya vimos cómo mostrar datos (output) a través de print().
¿Cómo ingresamos datos? Ingresar datos a nuestro programa se hace a través de
la función input().

La función input() es importante porque permite que nuestro programa sea más dinámico.
Tanto nosotros como nuestro usuario, podríamos interactuar con nuestra creación directamente.
Con input, podemos hacer que el usuario interactúe con el programa, pudiendo
escribir los datos que se desee ingresar.

NOTA:
- Empecemos a usar términos técnicos. Lo que va entre los paréntesis de las funciones
  se llama argumento -> funcion(argumento).

- Las entradas son muchas, podemos ingresar datos a través de cd's, usb, inclusive el mouse
  es una herramienta de entrada. Pero nosotros solo usaremos la entrada por teclado.

"""

edadUser = input('Ingresa tu edad...') # El usuario le dará valor a edadUser

"""
Veamos la anatomía de esta instrucción:

edadUser =: El dato ingresado se guardará en esta variable

input: Nombre de la función, indica que habrá una entrada

('Ingresa tu edad...'): Es un mensaje que se mostrará. Indica una instrucción.

NOTAS:
- La función input no debe tener argumentos. El mensaje es opcional y no afecta.

- El tipo de dato que almacena input siempre es una cadena o string
  (Cadena también es llamado string y nombrado como str.
  Cadena es igual a str).

"""



# ________________________________________________________________

numero = input()

"""
¿Qué sucede con la variable numero? Nosotros queremos que sea un número, pero
como dijimos anteriormente, input guarda cadenas. Aún si se ingresa un número
no será realmente un número. Sería '5', por ejemplo.

Esto se soluciona a través de conversión de datos o casting.
"""

miVariable = input()
miVariable = int(miVariable)

"""
En la línea 55 se hizo una instrucción de tipo casting
(de str(cadena) a  int(número entero)). La estructura del casting es siempre la misma
para convertir a otros tipos de datos: se indica la variable que queramos
convertir, seguido del símbolo de asignación (=),
el tipo de valor al que queramos convertir (int, en este caso)
y entre paréntesis la misma variable.
Aquí un índice de las abreviaturas de los tipo de datos:

- str (cadenas)
- int (número entero)
- float (número decimal)
- bool (booleano)
"""

miVariable = float(miVariable) # Convierte a decimal



# ________________________________________________________________

"""
Al igual que en print(), ¿se pueden hacer las mismas cosas en una línea?
Sí, se hace de la siguiente manera...
"""


pi = float(input())

# Esto es igual a...

pi = input()
pi = float(pi)



# ________________________________________________________________

"""
NOTA:
- Para que puedas ver el tipo de dato que es una variable...
  print(type(TuVariable))

  La salida será el tipo de dato que es esa variable (int, float, str, etc).
"""