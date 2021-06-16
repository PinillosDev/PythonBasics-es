"""
Las tuplas son una secuencia inmutable. Aquí sus características:

Como las listas, pueden contener los datos que queramos.
Como las listas, pueden ser recorridas con un ciclo for.
A diferencia de las listas, las tuplas no pueden modificar sus elementos. Es inmutable.

"""

unaVariable = 666

myTuple = (1, 'str', 3.876, ['a', 'b', 'c'], True, unaVariable) # Se crean entre paréntesis


numberTuple = 1, 2, 3, 4, 5, 6 # También puedes crear una tupla sin paréntesis
print('Este es el tipo de dato para numberTuple:', type(numberTuple))


for i in myTuple: # Una tupla puede ser recorrida con el ciclo for
    print(f'Un dato en la tupla: {i}')



otraTupla = 1, # Así creamos tuplas de un solo elemento. RECUERDA LA COMA (,)



# _______________________________________________________________________________



"""
¿Qué puedes hacer con tuplas?

- Permite indexar para ver su contenido.

- Usar la función len()

- + para sumar tuplas. * para multiplicar.

- Uso de in y not in

- Es el mejor tipo de dato para tener una gran cantidad de datos que no queremos que cambien
  durante la ejecución de un programa.

"""



# _______________________________________________________________________________



"""
Asignaciones y cambio de valores:

Es la manera en la que podemos guardar en variables, uno o más elementos de una tupla.

"""

tup = 1, 2, 3 # Se crea la tupla

a, b, c = tup # Ahora a=1, b=2 y c=3



# _______________________________________________________________________________



# Podemos hacer casting o conversión de datos


tup = tuple('Axell') # Strings -> tuple
print(tup) # Salida: ('A', 'x', 'e', 'l', 'l')

tup = tuple(['elemento', 123]) # list -> tuple
print(tup) # Salida: ('elemento', 123)

tup = tuple({'Mat': 30, 'Esp': 100}) # dictionary -> tuple
print(tup) # Salida: ('Mat', 'Esp')

# Los diccionarios (dictionary) los veremos en el próximo capítulo ;)