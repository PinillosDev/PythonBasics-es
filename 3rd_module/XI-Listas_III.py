"""
Comprensión de listas:

La comprensión de listas es básicamente otra forma de hacer listas. De esta forma nos vemos más
profesionales y ahorramos líneas de código.

"""


# De la siguiente forma se crea una lista, donde se rellena con un bucle for, donde el valor será de 2 * i
lista = [2 * i for i in range(11)]



# _______________________________________________________________________________



newList = [] # Se crea una lista

for i in range(21):
    if i % 2 == 0: # Si al dividir i entre dos el residuo es cero, entonces...
        newList.append(i) # Se agrega i a newList
    else:
        continue # De lo contrario, pasar a la siguiente cic


# El ciclo for hace lo mismo que la siguiente instrucción

lista2 = [i for i in range(21) if i % 2 == 0] # En una línea, se puede hacer lo mismo que en seis.



# _______________________________________________________________________________



"""
Arreglos bidimensionales:

Un arreglo bidimensional es una lista de listas. Es la forma en la que se crean y
representan tablas en Python.
Para crear un arreglo bidimensional usamos dos ciclos for, un ciclo para las filas
y otra para las columnas

"""


tabla = [[None for i in range(6)]for j in range(6)] # Se crea una tabla rellenada por None de 6 filas y 6 columnas


"""
Lo primero que llama la atención es el doble corchete. Recordemos que estamos haciendo unas lista dentro
de una lista, por lo que dentro de un par de corchetes se crea una lista y en el otro par la otra.

None es el elemento con el que se llenará el arreglo.

for i in range(6) es el ciclo con el que se crean las filas.
Por cada fila (ciclo de i) se hacen seis ciclos de j (for j in range(6)), que serán las columnas

Es decir, None for i in range(6) es como un piso de un edificio. Por cada piso se hace for j in range(6).

Las tablas son como un edificio, por cada piso (filas) se crea x cantidad de habitaciones (columnas)

"""



"""
¿Cómo se maneja un arreglo bidimensional?

Para ver, editar, ingresar y eliminar un arreglo bidimensional, solo se necesita un doble índice.
"""
print(tabla[2][3]) # De la tercera lista muestra al cuarto elemento


# _______________________________________________________________________________



"""
Arreglos tridimensionales

Es básicamente una lista dentro de la lista que está dentro de otra lista :)
Es decir, una lista 'a' que dentro de ella tiene a la lista 'b', que a su vez contiene a la lista 'c'.

Ejemplo de uso de un arreglo tridimensional:

Se necesita un programa que gestione la ocupación de un hotel. El hotel se estructura de 3 edificios, donde cada
edificio es de 15 pisos, donde cada piso es de 20 habitaciones.

"""


hotel = [
    [[False for habitación in range(20)]
    for pisos in range(15)]
    for edificio in range(3)]

# False porque al principio todas las habitaciones están vacías

hotel[2][4][12] = True # El 1er edificio del 3er piso de la 11va habitación está ocupado

# Recuerda que los índices empiezan desde cero. 2 no es 2, es 1 ;)



print(hotel)