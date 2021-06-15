# Tenemos la siguente función
def multiply(a, b):
    resultado = a * b
    return resultado

multiply(2, 4)


# print(resultado) Mostrará error. 'resultado' no existe. ¿Por qué,si la variable 'resultado'
# está adentro de la función 'multiply'?



"""
Definición de scopes:
El alcance de un nombre (de una variable) es la parte del código donde el
nombre es conocido correctamente.

Cuando se dice alcance, es como decir si se reconoce la existencia de x variable, ya sea dentro
o fuera de una función. Como es el caso de 'resultado', que NO se reconoce fuera de la definición.

"""



# _______________________________________________________________________________



# Una variable que existe fuera de una función tiene alcance dentro de una.

def resta(a):
    resultado = a - number
    return resultado

number = 2

"""
'number' tiene alcance dentro de una función. Mas sin embargo, nótese que solo se nombra
como elemento de una resta. El valor de 'number' NO está siendo alterado. 'number' seguirá
siendo 2.

"""



# _______________________________________________________________________________



# ¿Qué pasa si se altera el valor de una variable dentro de una función?

def divide(a):
    dividendo = 27 # Variable 'dividendo' dentro de función
    resultado = dividendo / 3
    return resultado


dividendo = 6 # Variable 'dividendo' fuera de función

print(dividendo) # ¿Cuál es la salida? ¿6 ó 27?


"""
Cuando una variable (creada fuera de una función) cambia su valor o directamente se le asigna
un valor (dentro de una fucnión) se crea una nueva variable.

def divide(a):
    dividendo = 27

Si una variable existente fuera de una función cambia su valor dentro de una función,
la función crea su propia variable; la cual tendrá alcance solo dentro de la función
y será diferente a la variable externa (a la primera).

Esta es la razón por la que print(dividendo) muestra 6 y no 27.

"""



# _______________________________________________________________________________



"""
¿Una función es capaz de modificar una variable que fue definida fuera de ella? Afortunadamente no.

Existe un método especial en Python el cual puede extender el alcance de una variable incluyendo
el cuerpo de las funciones para poder no solo leer los valores de las variables sino también
modificarlos.

Este efecto es causado por la palabra reservada llamada global.

"""

def boredFunction():
    global variable
    variable = 10


"""
El utilizar la palabra reservada dentro de una función con el nombre o nombres de las variables
separados por comas, obliga a Python a abstenerse de crear una nueva variable dentro de la función;
se empleará la que se puede acceder desde el exterior.

En otras palabras, este nombre se convierte en global (tiene un alcance global, y no importa
si se esta leyendo o asignando un valor).

"""