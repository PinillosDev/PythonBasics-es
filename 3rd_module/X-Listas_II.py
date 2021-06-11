"""
En este capítulo veremos más cosas interesantes acerca de las listas, como unos cuántos métodos.

"""



MyList = ['hola', 'mundo', 45, 1.2, True, 'alm', False, 'Soy un número'] # Se crea una lista con la que se trabajará



# MÉTODOS DE INSERCIÓN DE DATOS


# .append()
MyList.append('un nuevo dato :D') # Con .append() agregamos AL PRINCIPIO de la lista, en este caso 'un nuevo dato :D'


# .insert()
MyList.insert(3, 'otro elemento') # .insert(ubicación, elemento) agrega un elemento en la posición que queramos


print(MyList) # Ver el estado actual de la lista



# MÉTODOS DE ELIMINACIÓN DE DATOS


# .pop()
MyList.pop(2) # Elimina un elemento de acuerdo a su índice. Si se omite el índice, eliminará el último elemento


# .remove()
MyList.remove('otro elemento') # Elimina un elemento de acuerdo a su valor.



# _______________________________________________________________________________



# FUNCIONES Y MÉTODOS PARA LISTAS



MyList.reverse() # Revierte el contenido de la lista


print(len(MyList)) # La función len() nos muestra el tamaño de un dato


MyList.clear() # Vacía el contenido de una lista, es decir, la deja vacía


print(MyList)


"""
Hay muchas otras funciones y métodos para las listas, como .sort(), que ordena una lista.

Trata de construir un programa que use listas. Comúnmente investigando el cómo hacer algo nos encontramos
con funciones y métodos útiles.

"""



# _______________________________________________________________________________



# ¿Qué más podemos hacer con las listas?

"""
Operadores 'in' y 'not in'
¿Cómo hacemos para saber si x elemento está en una lista?
Esto lo hacemos a través de 'in' y 'not in'. Instrucciones que nos arrojarán un resultado de tipo bool.

"""

print(123 in MyList) # Salida: False. Porque 123 NO está en MyList

print('123' not in MyList) # Salida: True. Porque '123' NO está en MyList



# _______________________________________________________________________________



"""
listas + for

El ciclo for nos ayuda mucho con el manejo de listas, veámos cómo:
"""


for i in MyList: # Podemos ver los elementos de las listas
    print(i)


NumberList = [] # Se crea una lista vacía

for i in range(1, 101): # Podemos llenar una lista con range
    NumberList.append(i)


otraLista = []
number = 0

for i in range(6): # Crear listas con una variable que cambia de estado en la ejecución de un for
    number = number + i
    otraLista.append(number)



# _______________________________________________________________________________



"""
RODAJAS:

Las rodajas son un elemento de la sintaxis de Python y son de suma importancia.

Con las rodajas decimos: haz x cosa desde aquí hasta acá

¿Qué es x cosa?
Puede ser copiar o eliminar

Así se ve una rodaja:
[1:3]

Los números 1 y 3 son índices. La instrucción describe: haz x cosa desde 1 hasta 3.
Si omitimos los índices, será igual a decir: de principio a fin

"""


lista1 = NumberList[:] # Se crea 'lista1' y se copian los elementos de 'NumberList'

lista2 = NumberList[1:3] # Solo se copian ciertos elementos de NumberList

del lista1[1:3] # Se eliminan los elementos desde 1 hasta 3 de 'lista1'



"""
NOTA:
Para saber el índice del último elemento de una lista hay dos formas:

1) len(lista) te arroja el número de elementos y por ende el índice del útlimo elemento

2) -1 El número -1 es como decir: el primer elemento de derecha a izquierda

- Los índices negativos puedes ser perfectamente aplicables.
  -2 es el penúltimo elemento de una lista.

"""



# Simón, falta el último capítulo de listas. Son muy importantes, ten paciencia <3