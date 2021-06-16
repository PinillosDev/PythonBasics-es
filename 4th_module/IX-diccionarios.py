"""
DICCIONARIOS:
El diccionario es una estructura de datos NO SECUENCIAL (no se puede recorrer con for) pero
si es mutable. Es decir, puedes manipular los elementos que le conforman.

Al igual que los diccionarios de la vida real, se tiene una palabra y su equivalente. En Python
es igual. Tenemos una palabra (key) y su equivalente (value). Un diccionario es un conjunto de
claves (keys) y valores (values).

"""


myFirstDict = {
    'Dog': 'perro',
    'Cat': 'gato',
    'Fox': 'zorro',
    'Elephant': 'puente',
    'avión': 'airplane'
}


"""
myFirstDict - Es el nombre de nuestro diccionario. Podemos nombrarle como queramos.

{} - Los elementos de un diccionario van entre llaves

'Dog': 'perro'
  |       |
 key    value

, - Cada par de key y value debe finalizar con una coma (,). El último par no debe finalizar con ,
    Además, key y value deben ir separados por dos puntos (:)

"""



"""
NOTAS:

- Cada clave debe ser única

- Los diccionarios admiten todos los tipos de datos

- No es una lista. Una lista es enumerada, los diccionarios no. (No hay índice)

- len() retorna la cantidad de pares

- Un diccionario es una herramienta de un solo sentido

"""



# _______________________________________________________________________________



user0 = {
    'firstName': 'Juan',
    'lastName': 'Pinillos',
    'birthdate': '25/06/2002',
    'favoriteNumber': 37,
    'Casado': False
}



"""
¿Cómo utilizar un diccionario?

Los diccionarios los podemos manipular através de métodos y funciones. Hay herramientas que nos ayudan
a adoptar un diccionario para que pueda ser examinado por un bucle for.

.keys() - Retorna una lista de todas las claves dentro de un diccionario.

Función sorted() ordena la salida.
   for key in sorted(dict.keys())

Básicamente ordena la salida de las keys

.items() - Regresa una lista de tuplas donde cada tupla es un par de cada clave con su valor.
   for english, spanish in myFirstDict.items():
    print(english, '->', spanish)

.values() - Regresa solo la lista valores.

"""



# _______________________________________________________________________________



myFirstDict['Elephant'] = 'elefante' # Modificar un valor


myFirstDict['Bird'] = 'Pájaro' # Se agrega un nuevo par. La clave debe ser única.


myFirstDict.update({'Bird': 'pájaro'}) # Actualizar un par


del myFirstDict['avión'] # Elimina la clave junto con su valor