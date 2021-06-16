"""
Las tuplas son una secuencia inmutable, pero se pueden recorrer através de un bucle for.

"""

unaVariable = 666

myTuple = (1, 'str', 3.876, ['a', 'b', 'c'], True, unaVariable) # Se crean entre paréntesis


for i in myTuple: # Una tupla puede ser recorrida con el ciclo for
    print(f'Un dato en la tupla: {i}')



# _______________________________________________________________________________



"""
¿Qué puedes hacer con tuplas?

- Permite indexar para ver su contenido.

- Usar la función len()

- + para multiplicar tuplas. * para multiplicar.

- Uso de in y not in

- Es el mejor tipo de dato para tener una gran cantidad de datos que no queremos que cambien
  durante la ejecución de un programa.

"""



# _______________________________________________________________________________



otraTupla = 1, # Así creamo tuplas de un solo elemento

print(type(otraTupla))