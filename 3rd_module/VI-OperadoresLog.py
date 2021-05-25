"""
En este capítulo se trabajarán los operadores lógicos, que son una conexión de
condicionales. Es decir, la manera de evaluar dos o más condiciones a la vez.

Existen tres operadores lógicos: and, or y not.


Con and, que es un operador de conjunción, vemos si dos condiciones son verdaderas.

Con or, que es un operador de disyunción, vemos si al menos una condición es verdadera.

Con not, que es un operador de negación, cambiamos el valor a su opuesto.

"""


# Creamos estas dos variables que usaremos

var1 = True
var2 = False


# and
condition = var1 and var2


# or
condition = var1 or var2


# not
condition = not var1



"""
Es decir:

- and retorna True si ambas condiciones son verdaderas

- or retorna True si al menos una condición es verdadera

- not convierte True en False y False en True

"""



# __________________________________________________________________________________________


"""
El resultado de las operaciones lógicas se pueden estudiar mediante las siguientes tablas de verdades.


AND:

True and True = True
True and False = False
False and True = False
False and False = False

Solo se obtiene True si las dos condiciones son True


OR:

True or True = True
True or False = True
False or True = True
False or False = False

Se debe tener al menos un True para que nos de True


NOT:
not True = False
not False = True
"""



# __________________________________________________________________________________________


"""
Podemos operar con la lógica de más de dos condiciones.

Por ejemplo:

"""

var3 = True # Creamos una tercera variable

condition = var1 and var2 and var3

"""
Se calcula de la siguiente manera:
var1 (True) and var2 (False) = False. False and var3 (True) = False


Se puede realizar este proceso con varios operadores al mismo tiempo

"""

condition = var1 and var2 or var3 # ¿Qué resultado se obtiene? ¿True o False?